import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot

from routers.router_start import router_start

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_routers(
    router_start
)


async def on_startup():
    print('Успешный запуск бота')

async def main():
    await on_startup()
    await dp.start_polling(bot)


asyncio.run(main())