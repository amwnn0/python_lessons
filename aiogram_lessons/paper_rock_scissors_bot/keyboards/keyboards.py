from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram_lessons.paper_rock_scissors_bot.lexicon.lexicon import LEXICON_RU

accept_kb_builder = ReplyKeyboardBuilder()
accept_kb_builder.row(
    KeyboardButton(text=LEXICON_RU['y_button']),
    KeyboardButton(text=LEXICON_RU['n_button']),
    width=2
)
accept_keyboard = accept_kb_builder.as_markup(resize_keyboard=True)

choose_kb_builder = ReplyKeyboardBuilder()
choose_kb_builder.row(
    KeyboardButton(text=LEXICON_RU['paper']),
    KeyboardButton(text=LEXICON_RU['rock']),
    KeyboardButton(text=LEXICON_RU['scissors']),
    width=3
)
choose_keyboard = choose_kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
