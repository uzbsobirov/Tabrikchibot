from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

from data.config import CHANNELS
from keyboards.inline.main import main, admin_main
from data.config import ADMINS
from loader import dp, db, bot
from utils.misc.subscription import check


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id

    # Foydalanuvchini bazaga qo'shamiz
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            issubs='false'
        )

        # Adminga xabar beramiz
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\n"
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except:
        await bot.send_message(chat_id=ADMINS[0], text=f"{full_name} bazaga oldin qo'shilgan")


    rows = await db.select_row_panel()
    if len(rows) >= 1:
        # We check if user is not subs to channel
        for row in rows:
            status = await check(user_id=user_id, channel=row[1])
        if status == False:
            markup = InlineKeyboardMarkup(row_width=1)
            for channel in rows:
                chat = await bot.get_chat(channel[1])
                invite_link = await chat.export_invite_link()
                markup.insert(InlineKeyboardButton(text=chat.title, url=invite_link))
            markup.add(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'))

            text = f"<b>Assalomu aleykum</b>, {full_name}! Botdan to'liq foydalanish uchun homiy kanallarimizga a'zo " \
                   f"bo'ling"
            await message.answer(text=text, reply_markup=markup, disable_web_page_preview=True)
            await state.finish()

        else:
            if user_id != int(ADMINS[0]):
                text = f"Assalomu aleykum {full_name}! Botdan bemalol foydalanishingiz mumkin"
                await message.answer(text=text, reply_markup=main)
                await state.finish()
            else:
                text = f"Assalomu aleykum {full_name}! Botdan bemalol foydalanishingiz mumkin"
                await message.answer(text=text, reply_markup=admin_main)
                await state.finish()
    else:
        if user_id != int(ADMINS[0]):
            text = f"Assalomu aleykum {full_name}! Botdan bemalol foydalanishingiz mumkin"
            await message.answer(text=text, reply_markup=main)
            await state.finish()
        else:
            text = f"Assalomu aleykum {full_name}! Botdan bemalol foydalanishingiz mumkin"
            await message.answer(text=text, reply_markup=admin_main)
            await state.finish()