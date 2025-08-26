import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
import aiosqlite

db = None


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
    return ids
