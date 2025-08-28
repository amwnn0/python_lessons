import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats, BotCommandScopeChat, \
    BotCommandScopeChatAdministrators, BotCommandScopeChatMember
from load_dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

TARGET_CHAT_ID = -1001234567890
ADMIN_CHAT_ID = -1001234567890
TARGET_USER_ID = 112009012


# for all private chats
async def set_private_chat_commands(bot):
    commands = [
        BotCommand(command="menu", description="Показать меню"),
        BotCommand(command="profile", description="Мой профиль"),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())


# for all group chats
async def set_group_chat_commands(bot):
    commands = [
        BotCommand(command='rules', description='Правила чата'),
        BotCommand(command='report', description='Пожаловаться на спам')
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllGroupChats())


# for specific chat
async def set_specific_chat_commands(bot):
    commands = [
        BotCommand(command="vip_feature", description="Эксклюзивная функция"),
        BotCommand(command="support", description="Вызвать поддержку")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeChat(chat_id=TARGET_CHAT_ID))


# for admins
async def set_admin_chat_commands(bot):
    commands = [
        BotCommand(command="ban", description="Забанить пользователя"),
        BotCommand(command="unban", description="Разбанить пользователя")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeChatAdministrators(chat_id=ADMIN_CHAT_ID))


# for specific id in specific chat
async def set_personal_commands(bot):
    commands = [
        BotCommand(command="godmode", description="Режим бога"),
        BotCommand(command="broadcast", description="Сделать рассылку")
    ]
    await bot.set_my_commands(commands=commands,
                              scope=BotCommandScopeChatMember(chat_id=TARGET_CHAT_ID, user_id=TARGET_USER_ID))


# multilang commands
async def set_multilang_commands(bot):
    en_commands = [
        BotCommand(command="start", description="Launch"),
        BotCommand(command="help", description="Help")
    ]
    ru_commands = [
        BotCommand(command="start", description="Запуск"),
        BotCommand(command="help", description="Помощь")
    ]
    scope = BotCommandScopeAllPrivateChats()

    # set commands for en users
    await bot.set_my_commands(
        commands=en_commands,
        scope=scope,
        language_code="en"
    )

    # set commands for ru users
    await bot.set_my_commands(
        commands=ru_commands,
        scope=scope,
        language_code="ru"
    )


# dp.startup.register(set_personal_commands)
dp.startup.register(set_multilang_commands)
dp.startup.register(set_group_chat_commands)
# dp.startup.register(set_specific_chat_commands)
# dp.startup.register(set_admin_chat_commands)
dp.startup.register(set_private_chat_commands)

dp.run_polling(bot)
