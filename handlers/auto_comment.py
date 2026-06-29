from aiogram import F, types, Router
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from config import settings


auto_comment_router = Router()
auto_comment_router.message.filter(F.is_automatic_forward == True)

button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Чатик", url=settings.CHAT_URL), 
    InlineKeyboardButton(text="Буст каналу", url=settings.BOOST_URL)]
])

@auto_comment_router.message()
async def comment_cmd(message: types.Message):
    await message.reply_photo(photo=settings.COMMENT_BANNER_FILE_ID, reply_markup=button)