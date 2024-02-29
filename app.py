import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from router import router

bot = Bot(TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
