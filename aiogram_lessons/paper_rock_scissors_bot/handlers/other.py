from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram_lessons.paper_rock_scissors_bot.database.db import add_user
from aiogram_lessons.paper_rock_scissors_bot.filters.filters import IsNotKnownUser
from aiogram_lessons.paper_rock_scissors_bot.keyboards.keyboards import accept_keyboard

from aiogram_lessons.paper_rock_scissors_bot.lexicon.lexicon import LEXICON_RU

router = Router()
router.message.filter(IsNotKnownUser())


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start(new)'],
        reply_markup=accept_keyboard
    )
    await add_user(message.chat.id, message.from_user.first_name, message.from_user.username)
