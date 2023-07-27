-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT *
FROM crime_scene_reports; --See the full table

SELECT *
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = 'Humphrey Street'; --See the reports with the data we know.

SELECT *
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = 'Humphrey Street' AND description LIKE '%duck%'; --We also know that we are looking for a stolen duck.

-- 295 is the id of the report.
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

SELECT *
FROM interviews
WHERE transcript LIKE '%duck%'; --I am trying to find any interview in which the duck was discussed. (No results unlucky)

SELECT *
FROM interviews
WHERE month = 7 AND day = 28; --Looking for intewrviews in the same day the theft happened.

-- Eugene -> “I suppose,” said Holmes, “that when Mr. Windibank came back from France he was very annoyed at your having gone to the ball.”

-- Ruth -> Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

-- Eugene -> I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- Raymond -> As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

SELECT *
FROM atm_transactions
WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- ATM Transactions with the data from the Eugene interview.
--We dont know how many money.

/* +-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
| 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+ */

SELECT *
FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit';

-- Bakery security logs with the data from the Ruth interview

/* +-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+-----+------+-------+-----+------+--------+----------+---------------+ */

SELECT b.*, p.*
FROM bakery_security_logs b
JOIN people p
ON b.license_plate = p.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit';

-- The same query but I added the who owns each car.

/* +-----+------+-------+-----+------+--------+----------+---------------+--------+---------+----------------+-----------------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |   id   |  name   |  phone_number  | passport_number | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+--------+---------+----------------+-----------------+---------------+
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       | 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       | 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       | 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       | 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 268 | 2021 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
+-----+------+-------+-----+------+--------+----------+---------------+--------+---------+----------------+-----------------+---------------+ */

SELECT f.*, a.full_name AS 'Origin', d.full_name AS 'Destination'
FROM flights f
JOIN airports a
ON f.origin_airport_id = a.id
JOIN airports d
ON f.destination_airport_id = d.id
WHERE f.year = 2021 AND f.month = 7 AND f.day = 29 AND a.full_name LIKE 'Fiftyville%'
ORDER BY f.hour ASC, f.minute ASC
LIMIT 1;

-- With this query we get the earliest flight out of Fiftyville on 29 of July, we've got this data from the Raymond interview.

/* +----+-------------------+------------------------+------+-------+-----+------+--------+-----------------------------+-------------------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |           Origin            |    Destination    |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------------------------+-------------------+
| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------------------------+-------------------+ */

-- Now we know the flight they are goint to take and we also know the passports of the owners of the cars that left the parking.

SELECT p.*, pe.*
FROM passengers p
JOIN people pe
ON p.passport_number = pe.passport_number
WHERE p.flight_id = (
    SELECT f.id
    FROM flights f
    JOIN airports a
    ON f.origin_airport_id = a.id
    JOIN airports o
    ON f.destination_airport_id = o.id
    WHERE f.year = 2021 AND f.month = 7 AND f.day = 29 AND a.full_name LIKE 'Fiftyville%'
    ORDER BY f.hour ASC, f.minute ASC
    LIMIT 1
) AND p.passport_number IN (
    SELECT p.passport_number
    FROM bakery_security_logs b
    JOIN people p
    ON b.license_plate = p.license_plate
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit'
);

/* +-----------+-----------------+------+--------+--------+----------------+-----------------+---------------+
| flight_id | passport_number | seat |   id   |  name  |  phone_number  | passport_number | license_plate |
+-----------+-----------------+------+--------+--------+----------------+-----------------+---------------+
| 36        | 1695452385      | 3B   | 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
| 36        | 5773159633      | 4A   | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
| 36        | 8294398571      | 6C   | 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 36        | 8496433585      | 7B   | 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       |
+-----------+-----------------+------+--------+--------+----------------+-----------------+---------------+ */

SELECT *
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60
AND caller IN(
    SELECT pe.phone_number
    FROM passengers p
    JOIN people pe
    ON p.passport_number = pe.passport_number
    WHERE p.flight_id = (
        SELECT f.id
        FROM flights f
        JOIN airports a
        ON f.origin_airport_id = a.id
        JOIN airports o
        ON f.destination_airport_id = o.id
        WHERE f.year = 2021 AND f.month = 7 AND f.day = 29 AND a.full_name LIKE 'Fiftyville%'
        ORDER BY f.hour ASC, f.minute ASC
        LIMIT 1
    ) AND p.passport_number IN (
        SELECT p.passport_number
        FROM bakery_security_logs b
        JOIN people p
        ON b.license_plate = p.license_plate
        WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit'
    )
);

/* +-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
| 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
+-----+----------------+----------------+------+-------+-----+----------+ */


--Now we can guess the thief

SELECT name
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
WHERE flight_id = (
    SELECT id
    FROM flights
    WHERE
    day = "29"
    AND month = "7"
    AND year = "2021"
    ORDER BY hour, minute
    LIMIT 1
)
INTERSECT
SELECT DISTINCT name
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
JOIN atm_transactions
ON bank_accounts.account_number = atm_transactions.account_number
WHERE day = "28"
AND month = "7"
AND year = "2021"
AND transaction_type = "withdraw"
AND atm_location = "Leggett Street"
INTERSECT
SELECT name
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.caller
WHERE day = "28"
AND month = "7"
AND year = "2021"
AND duration < "60"
INTERSECT
SELECT name
FROM people
JOIN bakery_security_logs
ON people.license_plate = bakery_security_logs.license_plate
WHERE day = "28"
AND month = "7"
AND year = "2021"
AND hour = "10"
AND minute >= "15"
AND minute < "25"
AND activity = "exit";

-- The city the thief ESCAPED TO
SELECT d.city AS 'Destination City'
FROM flights f
JOIN airports a
ON f.origin_airport_id = a.id
JOIN airports d
ON f.destination_airport_id = d.id
WHERE f.year = 2021 AND f.month = 7 AND f.day = 29 AND a.full_name LIKE 'Fiftyville%'
ORDER BY f.hour ASC, f.minute ASC
LIMIT 1;


--And the accomplice
SELECT name
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE day = "28"
AND month = "7"
AND year = "2021"
AND duration < "60"
AND caller = (
    SELECT phone_number
    FROM people
    WHERE name = 'Bruce'
);