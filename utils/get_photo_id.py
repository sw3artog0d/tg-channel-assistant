from aiogram import types, F, Router
from aiogram.types import Message


photo_id_router = Router()

# Сохранение фото на сервере телеграм
@photo_id_router.message(F.photo)
async def get_photo_id(message: Message):
    photo_id = message.photo[-1].file_id
    print(message.photo)
    print(f"Ваш File ID: {photo_id}")
    await message.answer(f"ID вашего фото:\n`{photo_id}`", parse_mode="MarkdownV2")