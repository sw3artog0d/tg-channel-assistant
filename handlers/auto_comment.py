import logging
import asyncio

from aiogram import F, types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import settings, chats 

logger = logging.getLogger(__name__)

auto_comment_router = Router()
auto_comment_router.message.filter(F.is_automatic_forward == True)

media_group_tasks: dict[str, asyncio.Task] = {}

@auto_comment_router.message()
async def handle_incoming_message(message: types.Message):
    if message.media_group_id is None:
        await comment_cmd(message)
    else:
        if message.media_group_id not in media_group_tasks:
            media_group_tasks[message.media_group_id].cancel()
        media_group_tasks[message.media_group_id] = asyncio.create_task(answer_timer(message))

async def answer_timer(message: types.Message):
    await asyncio.sleep(settings.ALBUM_DEBOUNCE_SECONDS)
    try:
        await comment_cmd(message)
    except Exception:
        logger.exception("Ошибка при отправке комментария для media_group_id=%s", message.media_group_id)
    finally:
        del media_group_tasks[message.media_group_id]

async def comment_cmd(message: types.Message):
    chat_data = chats.get(str(message.chat.id))
    if chat_data is None:
        logger.warning(f"Чат {message.chat.id} не найден в chats.json, пропускаю")
        return
    
    builder = InlineKeyboardBuilder()
    builder.button(text="Чатик", url=chat_data["chat_url"])
    builder.button(text="Буст каналу", url=chat_data["boost_url"])
    builder.adjust(2)

    await message.reply_photo(photo=chat_data["comment_banner_file"], reply_markup=builder.as_markup())