import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from load_dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

# Initialize builder
kb_builder = ReplyKeyboardBuilder()

# Create buttons
contact_button = KeyboardButton(text='Share contact', request_contact=True)
geo_button = KeyboardButton(text='Share location', request_location=True)

# Add buttons to builder
kb_builder.row(contact_button, geo_button, width=1)

# Create keyboard
keyboard = kb_builder.as_markup(resize_keyboard=True)


# /start handler
@dp.message(CommandStart())
async def process_start_message(message: Message):
    await message.answer(
        text='Some experimental buttons',
        reply_markup=keyboard
    )


# Contact handler
@dp.message(F.contact)
async def process_contact_message(message: Message):
    await message.answer(
        text=f'Your phone number: {message.contact.phone_number}'
    )
    print(message.model_dump_json(indent=4, exclude_none=True))


# Geo handler
@dp.message(F.location)
async def process_location_message(message: Message):
    await message.answer(
        text=f'Your location: {message.location.latitude}, {message.location.longitude}'
    )
    print(message.model_dump_json(indent=4, exclude_none=True))


if __name__ == '__main__':
    dp.run_polling(bot)
