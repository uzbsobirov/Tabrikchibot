from aiogram.types import MediaGroup

from loader import dp, db, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="createcard", state='*')
async def create_card(call: types.CallbackQuery, state: FSMContext):
    album = MediaGroup()

    # Photo urls
    photo1_url = 'https://t.me/forchrabot/55'
    photo2_url = 'https://t.me/forchrabot/56'
    photo3_url = 'https://t.me/forchrabot/57'
    photo4_url = 'https://t.me/forchrabot/60'

    album.attach_photo(photo=photo1_url) # for first photo
    album.attach_photo(photo=photo2_url) # for second photo
    album.attach_photo(photo=photo3_url) # for third photo
    album.attach_photo(photo=photo4_url) # for fourth photo

    await call.message.answer_media_group(media=album)

