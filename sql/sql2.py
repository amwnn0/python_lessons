import sqlite3 as sq

cars = [
    ("Audi", 52642),
    ("Mersedes", 57127),
    ("Skoda", 9000),
    ("Volvo", 29000),
    ("Bentley", 350000),
]

with sq.connect("sql/cars.db") as con:
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS cars (
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                price INTEGER)"""
    )
    for car in cars:
        cur.execute("""INSERT INTO cars VALUES(NULL, ?, ?)""", car)
    cur.executemany("""INSERT INTO cars VALUES(NULL, ?, ?)""", cars)
    cur.execute("UPDATE cars SET price = :price WHERE model LIKE 'A%'", {"price": 100})
    cur.executescript(
        """DELETE FROM cars WHERE price == 100;
        UPDATE cars SET price = price+100000 WHERE model LIKE 'Be%'"""
    )
