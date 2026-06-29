from aiogram import Bot, Dispatcher
import asyncio

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