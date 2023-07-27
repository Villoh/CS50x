CREATE TABLE shares_bought (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    symbol TEXT NOT NULL,
    ammount INTEGER NOT NULL,
    price REAL NOT NULL,
    transacted DATETIME NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT FK_UsersShares FOREIGN KEY (user_id)
    REFERENCES users(id)
);
