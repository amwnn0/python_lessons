from aiogram.filters import BaseFilter
from aiogram.types import Message

from aiogram_lessons.paper_rock_scissors_bot.database.db import get_user_ids


class IsKnownUser(BaseFilter):
    async def __call__(self, message: Message):
        return message.from_user.id in await get_user_ids()
