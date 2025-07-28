import sqlite3 as sq


def read_ava(n):
    try:
        with open(f"sql/avas/{n}.png", "rb") as ava:
            return ava.read()
    except IOError as e:
        print(e)
        return False


def write_ava(name, data):
    try:
        with open(name, "wb") as ava:
            ava.write(data)
    except IOError as e:
        print(e)
        return False
    return True


with sq.connect("sql/cars.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM cars")

    for result in cur:
        print(result["model"], result["price"])

    cur.executescript(
        """CREATE TABLE IF NOT EXISTS users(
                      name TEXT,
                      ava BLOB,
                      score INTEGER)"""
    )

    img = read_ava(1)
    if img:
        binary = sq.Binary(img)
        cur.execute('INSERT INTO users VALUES ("Nikolay", ?, 1000)', (binary,))

    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()["ava"]
    write_ava("out.png", img)
