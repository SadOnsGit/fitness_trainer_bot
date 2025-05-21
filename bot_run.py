import os
import asyncio

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot

from routers.start_router import router_start

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

dp.include_routers(
    router_start
)

async def main():
    await dp.start_polling(bot)


asyncio.run(main())