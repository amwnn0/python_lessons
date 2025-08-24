import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from dotenv import load_dotenv
from random import randint
import asyncio
import aiohttp

import aiosqlite

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
app_storage = {}


async def on_startup():
    app_storage['db'] = await init_db()


async def on_shutdown():
    db = app_storage['db']
    await db.close()


async def init_db():
    db = await aiosqlite.connect('numbers.db')
    await db.execute('''CREATE TABLE IF NOT EXISTS users
                        (
                            chat_id PRIMARY KEY,
                            name TEXT NOT NULL,
                            username TEXT NOT NULL,
                            score INTEGER DEFAULT 0,
                            attempts INTEGER DEFAULT 5,
                            game_status BOOLEAN DEFAULT FALSE,
                            number INTEGER,
                            text TEXT,
                            games_played INTEGER DEFAULT 0,
                            games_won INTEGER DEFAULT 0
                        )''')
    await db.execute('''CREATE TABLE IF NOT EXISTS games
                        (
                            chat_id INTEGER NOT NULL,
                            number INTEGER NOT NULL,
                            guessed BOOLEAN DEFAULT FALSE
                        )''')
    await db.commit()
    return db


async def add_user_to_db(db, chat_id, name, username):
    try:
        await db.execute('''INSERT OR IGNORE INTO users (chat_id, name, username) VALUES (?, ?, ?)''',
                         (chat_id, name, username))
        await db.commit()
    except Exception as e:
        print(f'Database error: {e}')


async def get_number(chat_id) -> (int, str):
    number = randint(1, 100)
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://numbersapi.com/{number}')
        text = await response.text()
        words = text.split()
        words = words[2:]
        words[0] = words[0].capitalize()
        text = ' '.join(words)
    return number, text


@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    db = app_storage['db']
    chat_id = message.chat.id
    name = message.chat.first_name
    username = message.chat.username
    await add_user_to_db(db, chat_id, name, username)
    await db.execute(
        '''UPDATE users SET attempts = 5, game_status = False, number = NULL, text = NULL WHERE chat_id = ?''',
        (chat_id,))
    await db.commit()
    await message.answer(f'''
🎮 *Number Detective Challenge!* 🎮

I've picked a secret number between 1-100!  
🔍 I will give you hint about this number"  

You have *5 attempts* to guess it.  
🏆 *Score potential:* Up to 500 points!  

If you want to play, type "y", else type "n"
(Need help? Try /help)''')


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('''
🎯 OBJECTIVE:
Guess the secret number based on mathematical facts!
You have 5 attempts to find the correct number between 1-100.

📝 HOW TO PLAY:
1. I'll generate a random number (1-100) and give you a math fact about it
2. You send me your guess
3. I'll tell you if it's higher or lower
4. Repeat until you guess right or run out of attempts

➕ SCORING:
- Correct guess: +500 points
- Each attempt used: -100 points
Example: Guessing right on 3rd try = 500 - (2×100) = 300 points

💡 EXAMPLE:
My hint: "This number is a perfect square"
You guess: 25
I reply: "Higher!"
You guess: 36
I reply: "Correct! You earned 400 points!"

🎮 COMMANDS:
/start - Begin new game
/help - Show these instructions
/score - Check your total points''')


@dp.message(Command(commands='score'))
async def get_score(message: Message):
    db = app_storage['db']
    chat_id = message.chat.id
    async with db.execute('''SELECT score, games_played, games_won FROM users WHERE chat_id = ?''',
                          (chat_id,)) as cursor:
        data = await cursor.fetchone()
        score = data[0]
        games_played = data[1]
        games_won = data[2]
        await message.answer(f'''
🏅 Your Stats

🔢 Total games played: {games_played}  
🎯 Correct guesses: {games_won}
💰 Total points: {score}''')


@dp.message()
async def send_smth(message: Message):
    db = app_storage['db']
    chat_id = message.chat.id
    async with db.execute('''SELECT * FROM users WHERE chat_id = ?''', (chat_id,)) as cursor:
        data = await cursor.fetchone()
        score = data[3]
        attempts = data[4]
        game_status = data[5]
        number = data[6]
        text = data[7]
        games_played = data[8]
        games_won = data[9]
        if not game_status:
            if message.text.lower() == 'n':
                await message.answer(text='use /start command if you wanna play')

            # start of the game
            elif message.text.lower() == 'y':
                number, text = await get_number(chat_id)
                await cursor.execute(
                    '''UPDATE users SET game_status = True, number = ?, text = ?, games_played = ?
                    WHERE chat_id = ?''', (number, text, games_played + 1, chat_id))
                await db.commit()
                await message.answer(text=f'''
*Let's play! Type your first guess now, you have 5 attempts!*

{text}''')
            else:
                await message.answer(text='Type "y" or "n"\n(Need help? Try /help)')
        else:
            if attempts and message.text.lower() == str(number):
                await message.answer(text=f'You guessed right, congratulations, gain +{100 * attempts} score 🏆')
                await db.execute(
                    '''UPDATE users SET score = ?, attempts = 5, game_status = False, number = NULL, text = NULL, games_won = ? WHERE chat_id = ?''',
                    (score + 100 * attempts, games_won + 1, chat_id))
                await db.commit()
                await message.answer(text='If you want to play again, type "y"')
            elif attempts > 1:
                if int(message.text) < number:
                    text_hl = '📈 Too low'
                else:
                    text_hl = '📉 Too high'
                if abs(int(message.text) - number) <= 5:
                    text_hl = text_hl + ', 🔥 close'
                elif abs(int(message.text) - number) >= 20:
                    text_hl = text_hl + ', ❄️ far'
                await message.answer(
                    text=f'{text_hl}, {attempts - 1} attempt{'s' if attempts > 2 else ''} remaining')
                await db.execute('''UPDATE users SET attempts = ? WHERE chat_id = ?''', (attempts - 1, chat_id))
                await db.commit()
            # LOSE
            else:
                await message.answer(text=f'''
💥 *Game Over!*  

The number was *{number}*.  
({text})  

📌 You used all 5 attempts.  
Better luck next time!  

🔄 Want to try again? Type "y"
🏅 To see your stats: /score
📚 Need hints? /help ''')
                await cursor.execute(
                    '''UPDATE users SET game_status = False, attempts = 5, number = NULL, text = NULL WHERE chat_id = ?''',
                    (chat_id,))
                await db.commit()


async def main():
    await on_startup()
    try:
        await dp.start_polling(bot)
    finally:
        await on_shutdown()


if __name__ == '__main__':
    asyncio.run(main())
