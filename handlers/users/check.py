from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, db, bot
from utils.misc.subscription import check
from data.config import CHANNELS
from keyboards.inline.main import main
@dp.callback_query_handler(text="check_subs", state='*')
async def check_func(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    await call.answer("Obuna tekshirilmoqda...")
    final_status = True

    result = InlineKeyboardMarkup(row_width=1)

    for channel in CHANNELS:
        status = await check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        invite_link = await channel.export_invite_link()
        if status is not True:
            await db.update_user_issubs(user_id=user_id, issubs='false')
            final_status *= False
            result.insert(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))
    result.add(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'))

    if final_status:
        await db.update_user_issubs(user_id=user_id, issubs='true')
        await call.message.delete()
        await call.message.answer(text="<b>Xush kelibsiz! Bo'limlardan birini tanlang</b>", reply_markup=main)
        await state.finish()
    else:
        await call.message.delete()
        await call.message.answer(text="<b>❌Siz ba'zi kanallardan chiqib ketgansiz, agar kanallarga "
                                       "ulanmasangiz botni ishlata olmaysiz</b>", reply_markup=result,
                                    disable_web_page_preview=True)
        await state.finish()