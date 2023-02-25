from loader import dp
from states.one import Panel
from keyboards.inline.panel import panel
from keyboards.inline.main import admin_main

from aiogram import  types
from aiogram.dispatcher import FSMContext





@dp.callback_query_handler(text="orqaga", state=Panel.stat)
async def stat_back(call: types.CallbackQuery, state: FSMContext):
    text = "Admin panel bosh menyusi"
    await call.message.edit_text(text=text, reply_markup=panel)
    await state.finish()

@dp.callback_query_handler(text="orqaga", state=Panel.reklama)
async def stat_back(call: types.CallbackQuery, state: FSMContext):
    text = "Admin panel bosh menyusi"
    await call.message.edit_text(text=text, reply_markup=panel)
    await state.finish()

@dp.callback_query_handler(text="orqaga", state=Panel.majburiy)
async def stat_back(call: types.CallbackQuery, state: FSMContext):
    text = "Admin panel bosh menyusi"
    await call.message.edit_text(text=text, reply_markup=panel)
    await state.finish()

@dp.callback_query_handler(text="orqaga", state='*')
async def stat_back(call: types.CallbackQuery, state: FSMContext):
    text = "Asosiy menu"
    await call.message.edit_text(text=text, reply_markup=admin_main)
    await state.finish()