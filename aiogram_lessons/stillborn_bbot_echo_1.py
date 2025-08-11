import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from load_dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer('Hello, write smth')


async def process_help_command(message: Message):
    await message.answer('Write smth, ill answer')


async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


async def send_animation_echo(message: Message):
    await message.reply_audio(message.animation.file_id)


async def send_voice_echo(message: Message):
        await message.reply_audio(message.voice.file_id)


async def send_document_echo(message: Message):
    await message.reply_audio(message.document.file_id)


async def send_echo(message: Message):
    await message.reply(text=message.text)


dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_animation_echo, F.animation)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
