import os

from aiogram import Bot, Dispatcher
from aiogram.types import KeyboardButton, KeyboardButtonRequestUser, KeyboardButtonRequestUsers, \
    KeyboardButtonRequestChat, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from load_dotenv import load_dotenv
from pkg_resources import resource_isdir

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

request_user_button = KeyboardButton(
    text='Request user',
    request_user=KeyboardButtonRequestUser(
        request_id=42,
        user_is_premium=False
    )
)

request_users_button = KeyboardButton(
    text='Request users',
    request_users=KeyboardButtonRequestUsers(
        request_id=77,
        user_is_premium=False,
        max_quantity=10
    )
)

request_chat_button = KeyboardButton(
    text='Request user',
    request_chat=KeyboardButtonRequestChat(
        request_id=1408,
        chat_is_channel=False,
        chat_is_forum=False
    )
)

kb_builder.row(request_user_button, request_users_button, request_chat_button, width=1)
keyboard = kb_builder.as_markup(
    resize_keyboard=True,
)


@dp.message
async def process_start_command(message: Message):
    await message.answer(
        text='Some special buttons',
        reply_markup=keyboard
    )


@dp.message(...)
async def process_user_shared(message: Message):
    ...
