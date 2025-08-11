import os

import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from load_dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_URL = os.getenv('API_URL')


def connect() -> dict:
    print(f'Attempt {COUNTER}')
    data = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={OFFSET}&timeout=50').json()
    return data


def main():
    global COUNTER
    global OFFSET
    COUNTER = 1
    MAX_COUNT = 2
    OFFSET = -1
    while COUNTER < MAX_COUNT:
        data = connect()
        if data['result']:
            for update in data['result']:
                chat_id = data['message']['chat']['id']

                OFFSET = update['update_id'] + 1
                COUNTER += 1


if __name__ == '__main__':
    main()
