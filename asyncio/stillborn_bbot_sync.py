import os

import requests
from load_dotenv import load_dotenv
from time import sleep


load_dotenv()
TOKEN = os.getenv('TOKEN')
API_URL = os.getenv('API_URL')


def connect() -> dict:
    print(f'Attempt {COUNTER}, connecting to {API_URL}')
    data = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={OFFSET}&timeout=50').json()
    return data

def send_message(chat_id, text):
    print(f'Sending message {COUNTER}, wait for a second...')
    sleep(3)
    requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
    print(f'Message {COUNTER} sent')

def main():
    global COUNTER
    global OFFSET
    COUNTER = 1
    MAX_COUNT = 5
    OFFSET = -1
    while COUNTER < MAX_COUNT:
        data = connect()
        if data['result']:
            for update in data['result']:
                chat_id = update['message']['chat']['id']
                message = update['message']['text']
                send_message(chat_id, message)
                OFFSET = update['update_id'] + 1
                COUNTER += 1


if __name__ == '__main__':
    main()
