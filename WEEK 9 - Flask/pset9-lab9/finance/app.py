import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    shares_bought = db.execute(
        "SELECT symbol,  SUM(ammount) as total_shares FROM shares_bought WHERE user_id = ? GROUP BY symbol HAVING SUM(ammount) > 0", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    total_shares = sum(map(lambda share_bought: lookup(share_bought['symbol'])[
        'price'] * share_bought['total_shares'], shares_bought))
    total_cash = cash + total_shares

    return render_template("index.html", shares_bought=shares_bought, lookup=lookup, cash=cash, total_cash=total_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Get the share symbol from the user input
        symbol = request.form.get("symbol")
        # Check if the sybol exists
        if symbol:
            # Get the share data from the API
            quote = lookup(symbol)
            # Check if the share exist in the API
            if quote:
                # Assign all the values
                shares = request.form.get("shares")

                if not shares.isdigit():
                    return apology("Invalid number of shares", 400)

                if int(shares) <= 0:
                    return apology("Shares must be a positive number", 400)

                user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
                price = quote["price"]
                total_cost = price * int(shares)
                # Check if the user has the money to buy the shares
                if user_cash >= total_cost:
                    # Update symbool just in case and insert the share
                    symbol = quote["symbol"]
                    try:
                        db.execute("INSERT INTO shares_bought (symbol, ammount, price, transacted, user_id) VALUES(?, ?, ?, ?, ?)",
                                   symbol, int(shares), price, datetime.now(), session["user_id"])
                        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, session["user_id"])
                        flash("Bought!", "success")
                        return index()
                    except Exception:
                        return apology("error while buying the shares", 400)
                else:
                    return apology("you don't have enough cash", 400)
            else:
                return apology("invalid symbol", 400)
        else:
            return apology("missing symbol", 400)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    shares_bought = db.execute("SELECT * FROM shares_bought WHERE user_id = ?", session["user_id"])
    return render_template("history.html", shares_bought=shares_bought)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Get the share symbol from the user input
        symbol = request.form.get("symbol")
        # Check if the sybol exists
        if symbol:
            # Get the share data from the API
            quote = lookup(symbol)
            # Check if the share exist in the API
            if quote:
                # Assign all the values
                name = quote["name"]
                price = usd(quote["price"])  # This one formatted to USD
                symbol = quote["symbol"]
                return render_template("quoted.html", name=name, price=price, symbol=symbol)
            else:
                return apology("invalid symbol", 400)
        else:
            return apology("missing symbol", 400)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get all the data from the request
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure password was submitted
        elif not confirmation:
            return apology("must provide password", 400)

        # Ensure password is equals to Confirmation
        elif password != confirmation:
            return apology("Passwords don't match", 400)

        # Ensure user dosn't exist
        user_exists = check_username(username)

        if user_exists == True:
            return apology("username already exists", 400)

        # Insert the new user
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Get the share symbol from the user input
        symbol = request.form.get("symbol")
        # Check if the sybol exists
        if symbol:
            # Assign all the values
            shares = request.form.get("shares")

            # Check if it's an int
            if not shares.isdigit():
                return apology("Invalid number of shares", 400)

            if int(shares) <= 0:
                return apology("Shares must be a positive number", 400)

            shares_ammount = db.execute("SELECT SUM(ammount) FROM shares_bought WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)[
                0]["SUM(ammount)"]
            if shares_ammount >= int(shares):
                price = lookup(symbol)["price"]
                db.execute("INSERT INTO shares_bought (symbol, ammount, price, transacted, user_id) VALUES(?, ?, ?, ?, ?)",
                           symbol, -int(shares), price, datetime.now(), session["user_id"])
                db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", price * int(shares), session["user_id"])
                flash("Sold!", "success")
                return index()
            else:
                return apology("you don't have that ammount of shares", 400)
        else:
            return apology("missing symbol", 400)
    else:
        rows = db.execute(
            "SELECT DISTINCT(symbol) FROM shares_bought WHERE user_id = ? GROUP BY symbol HAVING SUM(ammount) > 0;", session["user_id"])
        # Extract the symbols from the rows into a list using list comprehension
        symbols = [row["symbol"] for row in rows]
        return render_template("sell.html", symbols=symbols)


def check_username(username):
    # Check if the username already exists in the database
    result = db.execute("SELECT COUNT(*) FROM users WHERE username = ?", username)

    if result[0]['COUNT(*)'] == 1:
        user_exists = True
    else:
        # If the query did not return any result, consider the username as not existing
        user_exists = False
    # Return the result as JSON to the client
    return user_exists


@app.route("/check_username/<username>")
def check_username_route(username):
    # Get the result from the check_username function
    user_exists = check_username(username)

    # Return the result as JSON to the client
    return jsonify({"exists": user_exists})


@app.errorhandler(404)
def page_not_found(e):
    # You can render a custom template or return a JSON response, as needed.
    # In this example, we render a simple HTML page with a "Not Found" message.
    return apology("page not found", 404)

