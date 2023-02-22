from keyboards.inline.main import range_numbers
from loader import dp, db, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="createcard", state='*')
async def create_card(call: types.CallbackQuery, state: FSMContext):

    # Photo urls
    photo1_url = 'https://t.me/forchrabot/55'
    photo2_url = 'https://t.me/forchrabot/56'
    photo3_url = 'https://t.me/forchrabot/57'
    photo4_url = 'https://t.me/forchrabot/60'

    await call.message.answer_photo(photo=photo1_url, caption="Keraklisini tanlang: ", reply_markup=range_numbers())
    print(range_numbers())


