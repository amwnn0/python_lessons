import sqlite3 as sq

with sq.connect("sql/cars.db") as con:
    cur = con.cursor()

    # with open("sql_damp.sql", "wt") as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    with open("sql_damp.sql", "rt") as f:
        cur.executescript(f.read())
