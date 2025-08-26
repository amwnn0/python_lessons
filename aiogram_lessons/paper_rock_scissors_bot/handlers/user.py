from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_lessons.modular_echo_bot.lexicon.lexicon import LEXICON_RU
from aiogram_lessons.paper_rock_scissors_bot.filters.filters import IsKnownUser

router = Router()

# Filter router for known users
router.message.filter(IsKnownUser())


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
