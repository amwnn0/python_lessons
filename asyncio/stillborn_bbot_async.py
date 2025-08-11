import os

import requests
from load_dotenv import load_dotenv
import asyncio
from aiohttp import ClientSession
import ssl
import certifi

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_URL = os.getenv('API_URL')
ssl_context = ssl.create_default_context(cafile=certifi.where())

async def send_message(chat_id, text):
    print(f'Sending message {text}, wait for a second...')
    await asyncio.sleep(4)
    requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
    print(f'Message {text} sent')

async def main():
    global COUNTER
    global OFFSET
    COUNTER = 1
    MAX_COUNT = 20
    OFFSET = -1
    while COUNTER < MAX_COUNT:
        async with ClientSession() as session:
            url = f'{API_URL}{TOKEN}/getUpdates?offset={OFFSET}&timeout=50'
            async with session.get(url, ssl=ssl_context) as response:
                data = await response.json()
                if data['result']:
                    tasks = []
                    for update in data['result']:
                        chat_id = update['message']['chat']['id']
                        message = update['message']['text']
                        tasks.append(asyncio.create_task(send_message(chat_id, message)))
                        OFFSET = update['update_id'] + 1
                        COUNTER += 1
                    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())