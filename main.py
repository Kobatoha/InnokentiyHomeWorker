import os
import requests
import datetime
from lowadi import *
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'


LESSONS_TODAY = [
    '08:00 - Математика',
    '09:00 - Английский язык',
    '10:00 - Химия',
    '11:00 - История',
    '12:00 - Физика'
]

LESSONS_TOMORROW = [
    '08:00 - Биология',
    '09:00 - География',
    '10:00 - Литература',
    '11:00 - Информатика',
    '12:00 - Физкультура'
]


def get_updates():
    """Функция для получения обновлений (сообщений) от Telegram API"""
    url = BASE_URL + 'getUpdates'
    response = requests.get(url)
    return response.json()


def send_message(chat_id, text):
    """Отправка сообщения пользователю"""
    url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)


def get_lesson_schedule():
    """Получить расписание в зависимости от времени запроса"""
    current_time = datetime.datetime.now().time()
    # Сравниваем текущее время с 08:00
    if current_time < datetime.time(8, 0):
        return 'Сегодняшние уроки:\n' + '\n'.join(LESSONS_TODAY)
    else:
        return 'Завтрашние уроки:\n' + '\n'.join(LESSONS_TOMORROW)


def handle_message(message):
    """Обработка входящего сообщения"""
    chat_id = message['chat']['id']
    text = message['text']

    if text == '/lessons':
        lesson_schedule = get_lesson_schedule()
        send_message(chat_id, lesson_schedule)
    else:
        send_message(chat_id, 'Команда не распознана. Используйте /lessons для получения расписания.')


def main():
    last_update_id = None

    while True:
        updates = get_updates()

        if updates['ok']:
            for update in updates['result']:
                # Обрабатываем только новые сообщения
                if last_update_id is None or update['update_id'] > last_update_id:
                    last_update_id = update['update_id']
                    handle_message(update['message'])


if __name__ == '__main__':
    main()
