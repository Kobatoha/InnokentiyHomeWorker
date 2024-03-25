import asyncio
import sys
from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from lowadi import *

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {message.from_user.full_name}!")

@dp.message(command='work_horse')
async def work_horses():
    print('Запускаем прогон лошадулек')
    work_horse()

    await message.answer(f'Запускаем прогон лошадулек')


async def login_horses():
    print('Open')


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
