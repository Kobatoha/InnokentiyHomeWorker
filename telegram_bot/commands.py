import aiohttp
import asyncio
import datetime

import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'


async def get_updates(session):
    """Функция для получения обновлений (сообщений) от Telegram API"""
    async with session.get(BASE_URL + 'getUpdates') as response:
        return await response.json()


async def send_message(session, chat_id, text):
    """Отправка сообщения пользователю"""
    url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={text}'
    async with session.get(url) as response:
        return await response.json()




