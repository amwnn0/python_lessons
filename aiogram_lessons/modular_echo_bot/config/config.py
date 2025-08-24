import os
from dataclasses import dataclass
from load_dotenv import load_dotenv


@dataclass
class TgBot:
    token: str


@dataclass
class LogSettings:
    level: str
    format: str


@dataclass
class Config:
    bot: TgBot
    log: LogSettings


def load_config() -> Config:
    load_dotenv()
    return Config(
        bot=TgBot(token=os.getenv("BOT_TOKEN")),
        log=LogSettings(level=os.getenv("LOG_LEVEL"), format=os.getenv("LOG_FORMAT"))
    )
