import aiohttp
import asyncio
import datetime
from telegram_bot.commands import *
from todo.lessons import *
import os
from dotenv import load_dotenv

from lowadi import *

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_lesson_schedule():
    """Получить расписание в зависимости от времени запроса"""
    current_time = datetime.datetime.now().time()
    day = datetime.datetime.now().strftime('%A')
    # Сравниваем текущее время с 13:00
    if current_time < datetime.time(13, 0):
        return 'Сегодняшние уроки:\n' + '\n'.join(lesson_Dima[day])
    else:
        return 'Завтрашние уроки:\n' + '\n'.join(lesson_Dima[day])


async def handle_message(session, message):
    """Обработка входящего сообщения"""
    chat_id = message['chat']['id']
    text = message['text']

    if text == '/lessons':
        lesson_schedule = get_lesson_schedule()
        await send_message(session, chat_id, lesson_schedule)
    else:
        await send_message(session, chat_id, 'Команда не распознана. Используйте /lessons для получения расписания.')


async def main():
    last_update_id = None

    async with aiohttp.ClientSession() as session:
        while True:
            updates = await get_updates(session)

            if updates['ok']:
                for update in updates['result']:
                    # Обрабатываем только новые сообщения
                    if last_update_id is None or update['update_id'] > last_update_id:
                        last_update_id = update['update_id']
                        await handle_message(session, update['message'])
            # Задержка перед следующим запросом к API
            await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
