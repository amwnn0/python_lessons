import sqlite3 as sq


with sq.connect("sql/lesson.db") as db:
    cur = db.cursor()
    # cur.execute("""DROP TABLE IF EXISTS users""")
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
                name TEXT NOT NULL,
                sex INTEGER DEFAULT 1,
                age INTEGER NOT NULL, 
                score INTEGER DEFAULT 0
                )"""
    )

    # cur.execute("""INSERT INTO users VALUES('Name', 1, 44, 10000)""")
    cur.execute(
        """SELECT * FROM users WHERE score >=1000 AND sex == 1 ORDER BY score DESC LIMIT 3"""
    )
    res1 = cur.fetchone()
    res2 = cur.fetchmany(2)
    res3 = cur.fetchall()
    print(res1, res2, res3, sep="\n")

    cur.execute("""UPDATE users SET score = 0 WHERE sex ==0""")
    cur.execute("""UPDATE users SET age = age+1 WHERE name LIKE 'M_n%'""")
    cur.execute("""UPDATE users SET age = 30, score = 1480 WHERE age <=20""")

    cur.execute("""DELETE FROM users WHERE name == 'Man'""")

    cur.execute(
        """CREATE TABLE IF NOT EXISTS games(
                user_id INTEGER,
                score INTEGER DEFAULT 0,
                time INTEGER DEFAULT 0
                )"""
    )
    cur.execute("""SELECT count() as cnt FROM games WHERE user_id = 1""")
    print(cur.fetchall())
    cur.execute("""SELECT count(DISTINCT user_id) as cnt FROM games""")
    print(cur.fetchall())
    cur.execute("""SELECT sum(score) as sum FROM games WHERE user_id == 1""")
    print(cur.fetchall())
    cur.execute("""SELECT max(score) as mx FROM games WHERE user_id == 1""")
    print(cur.fetchall())

    cur.execute(
        """SELECT user_id, sum(score) as sum
    FROM games
    WHERE score > 300
    GROUP BY user_id
    ORDER BY sum DESC
    LIMIT 1"""
    )
    print(cur.fetchall())

    cur.execute(
        """SELECT name, sex, games.score FROM games
    JOIN users ON games.user_id = users.ROWID"""
    )
    print(cur.fetchall())

    # вывод топ по сумме счета привязка имени и пола по userid
    cur.execute(
        """SELECT name, sex, sum(games.score) as sum
    FROM games
    JOIN users ON games.user_id = users.ROWID
    GROUP BY user_id
    ORDER BY sum DESC"""
    )
    print(cur.fetchall())

    # join tables
    cur.execute(
        """SELECT score, "from" FROM tab1
    UNION SELECT val, type FROM tab2"""
    )
    cur.execute(
        """SELECT score, 'table 1' as tbl FROM tab1
    UNION SELECT val, 'table 2' FROM tab2
    LIMIT 3"""
    )

    cur.execute(
        """SELECT name, subject, mark FROM marks
    JOIN students ON students.id = marks.id
    WHERE mark>(SELECT mark FROM marks WHERE id=2 AND subject='C') AND subject='C'"""
    )

    """INSERT INTO fem_students
    SELECT * FROM students WHERE sex=0"""

    """DELETE FROM students
    WHERE age <= (SELECT age FROM students WHERE id=2)"""
