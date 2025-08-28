from random import randint

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from aiogram_lessons.paper_rock_scissors_bot.keyboards.keyboards import accept_keyboard, choose_keyboard
from aiogram_lessons.paper_rock_scissors_bot.lexicon.lexicon import LEXICON_RU
from aiogram_lessons.paper_rock_scissors_bot.filters.filters import IsKnownUser
from aiogram_lessons.paper_rock_scissors_bot.services.services import get_winner

router = Router()

# Filter router for known users
router.message.filter(IsKnownUser())


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=accept_keyboard
    )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(F.text == LEXICON_RU['y_button'])
async def process_y_button(message: Message):
    await message.answer(
        text=LEXICON_RU['accept_text'],
        reply_markup=choose_keyboard
    )


@router.message(F.text == LEXICON_RU['n_button'])
async def process_n_button(message: Message):
    await message.answer(text=LEXICON_RU['decline_text'])


@router.message(F.text.in_([LEXICON_RU['paper'], LEXICON_RU['rock'], LEXICON_RU['scissors']]))
async def process_game_answer(message: Message):
    await message.answer(text=get_winner(message.text))
    await message.answer(text=LEXICON_RU['play_again'], reply_markup=accept_keyboard)


# For other messages
@router.message()
async def process_other_message(message: Message):
    await message.answer(text=LEXICON_RU['other'])
