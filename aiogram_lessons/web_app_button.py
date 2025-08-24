import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, Message, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardMarkup
from load_dotenv import load_dotenv


load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

# Create button
web_app_button = KeyboardButton(
    text='Web app button',
    web_app=WebAppInfo(url="https://stepik.org/")
)

# Create keyboard object
keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_button]],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Web app button',
        reply_markup=keyboard
    )


@dp.message(Command(commands='web_app'))
async def process_web_app(message: Message):
    await message.answer(
        text='Web app button',
        reply_markup=keyboard
    )

if __name__ == '__main__':
    dp.run_polling(bot)