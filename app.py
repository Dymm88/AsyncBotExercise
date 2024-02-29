import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
