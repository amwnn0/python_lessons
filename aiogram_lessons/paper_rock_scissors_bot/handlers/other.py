from aiogram import Router
from aiogram.types import Message
from aiogram_lessons.modular_echo_bot.lexicon.lexicon import LEXICON_RU

router = Router()


@router.message()
async def process_message(message: Message):
    ...
