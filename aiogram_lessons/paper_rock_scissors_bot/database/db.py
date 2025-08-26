import aiosqlite


async def init_db():
    global db
    db = await aiosqlite.connect('p_r_s.db')
    await db.execute('''CREATE TABLE IF NOT EXISTS users 
                        (
                            chat_id PRIMARY KEY,
                            name TEXT NOT NULL,
                            username TEXT NOT NULL,
                            score INTEGER DEFAULT 0,
                            game_status BOOLEAN DEFAULT FALSE
                        )''')
    await db.commit()
    return db


async def get_user_ids():
    async with db.execute('''SELECT chat_id FROM users''') as cursor:
        ids = await cursor.fetchall()
    return [id[0] for id in ids]


async def add_user(chat_id, first_name, username):
    await db.execute('''INSERT INTO users (chat_id, name, username) VALUES (?, ?, ?)''',
                     (chat_id, first_name, username))
    await db.commit()
