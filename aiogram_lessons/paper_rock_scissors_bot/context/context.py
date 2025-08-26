from aiogram_lessons.paper_rock_scissors_bot.database.db import init_db


class AppContext:
    def __init__(self):
        self.db = None

    async def initialize(self):
        self.db = await init_db()

    async def close(self):
        if self.db:
            self.db.close()


app_context = AppContext()
