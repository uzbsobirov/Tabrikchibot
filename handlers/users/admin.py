import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.panel import panel


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="@BekoDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

@dp.callback_query_handler(text="adminpanel", state='*', user_id=ADMINS)
async def admin_panel(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Admin panelga xush kelibsiz👣", reply_markup=panel)
    await state.finish()