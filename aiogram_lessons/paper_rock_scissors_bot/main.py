import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import other, user
from context.context import app_context


async def main() -> None:
    # Load config
    config = load_config()
    # Set basic logging config
    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format
    )
    # Initialize bot and dispatcher
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()
    # Initialize context
    await app_context.initialize()
    dp['app_context'] = app_context
    # Register routers in dp
    dp.include_router(user.router)
    dp.include_router(other.router)
    # Skip updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
