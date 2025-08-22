from aiogram import Router
from aiogram.types import Message
from aiogram_lessons.modular_echo_bot.lexicon.lexicon import LEXICON_RU

router = Router()


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
