import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import BaseFilter
from aiogram.types import Message
from load_dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
admin_ids: list[int] = [112009012]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message):
        return message.from_user.id in self.admin_ids


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            word = word.strip('.,')
            if word.isdigit():
                numbers.append(int(word))
        if numbers:
            return {'numbers': numbers}
        else:
            return False


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа
@dp.message(F.text.lower().startswith('find numbers'), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]) -> None:
    await message.answer(f'Found numbers: {" ,".join(map(str, numbers))}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(F.text.lower().startswith('find numbers'))
async def process_if_not_numbers(message: Message) -> None:
    await message.answer('Numbers not found')


@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text=f'''You are administrator!''')


@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text=f'''You are not administrator!''')


dp.run_polling(bot)
