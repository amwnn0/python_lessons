import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from load_dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher()

# Create buttons
button1 = KeyboardButton(text='Собак 🦮')
button2 = KeyboardButton(text='Огурцов 🥒')

# Create keyboard
keyboard = ReplyKeyboardMarkup(keyboard=[[button1, button2]], resize_keyboard=True)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего кошки боятся больше?',
        reply_markup=keyboard
    )


@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше',
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
        reply_markup=ReplyKeyboardRemove()
    )


if __name__ == '__main__':
    dp.run_polling(bot)
