import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from load_dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Hello, write smth')


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('Write smth, ill answer')


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
