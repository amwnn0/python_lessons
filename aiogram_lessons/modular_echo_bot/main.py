import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram_lessons.modular_echo_bot.config.config import load_config, TgBot


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
    # Skip updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
