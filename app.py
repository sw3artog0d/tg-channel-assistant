from aiogram import Bot, Dispatcher
import asyncio
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler("place_bot.log", maxBytes=5_000_000, backupCount=3, encoding="utf-8")
    ]
)

from config import settings
from handlers.auto_comment import auto_comment_router
from utils.get_photo_id import photo_id_router


bot = Bot(token=settings.BOT_TOKEN)

dp = Dispatcher()

dp.include_router(auto_comment_router)
# dp.include_router(photo_id_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())