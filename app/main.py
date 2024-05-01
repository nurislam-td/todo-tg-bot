import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.settings import settings
from app.handlers.tasks import router as task_router
from app.handlers.common import router as common_router

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(task_router)
dp.include_router(common_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
