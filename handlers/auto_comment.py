from aiogram import F, types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import settings, chats  


auto_comment_router = Router()
auto_comment_router.message.filter(F.is_automatic_forward == True)

@auto_comment_router.message()
async def comment_cmd(message: types.Message):
    chat_data = chats.get(str(message.chat.id))
    
    builder = InlineKeyboardBuilder()
    builder.button(text="Чатик", url=chat_data["chat_url"])
    builder.button(text="Буст каналу", url=chat_data["boost_url"])
    builder.adjust(2)

    await message.reply_photo(photo=chat_data["comment_banner_file"], reply_markup=builder.as_markup())