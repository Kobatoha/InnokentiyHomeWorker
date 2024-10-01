import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_updates():
    """Функция для получения обновлений (сообщений) от Telegram API"""
    url = BASE_URL + 'getUpdates'
    response = requests.get(url)
    return response.json()


def send_message(chat_id, text):
    """Отправка сообщения пользователю"""
    url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)


