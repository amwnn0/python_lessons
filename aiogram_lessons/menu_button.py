import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from load_dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def set_main_menu(bot):
    main_menu_commands = [
        BotCommand(command='help',
                   description='...help'),
        BotCommand(command='start',
                   description='...start'),
        BotCommand(command='contacts',
                   description='...contacts')
    ]
    await bot.set_my_commands(main_menu_commands)


dp.startup.register(set_main_menu)

dp.run_polling(bot)
