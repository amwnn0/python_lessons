import sqlite3 as sq

con = None
try:
    con = sq.connect("sql/cars.db")
    cur = con.cursor()

    cur.executescript(
        """CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER);
        BEGIN;
        
        DELETE FROM cars WHERE price == 100;
        UPDATE cars SET price = price+100000 WHERE model LIKE 'Be%'"""
    )

    con.commit()

except sq.Error as e:
    if con:
        con.rollback()
    print("ERROR")
finally:
    if con:
        con.close()
