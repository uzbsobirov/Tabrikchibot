from PIL import Image, ImageDraw, ImageFont

from keyboards.inline.main import range_numbers, share
from loader import dp, db, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.one import Type
@dp.callback_query_handler(text="createcard", state='*')
async def create_card(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    # Photo urls
    with open('media/main.png', 'rb') as photo:
        await call.message.answer_photo(photo=photo, caption="Keraklisini tanlang: ", reply_markup=range_numbers())


@dp.callback_query_handler(text="1-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type1.set()

@dp.message_handler(state=Type.type1)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/1-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 62)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = (img.width - text_size[2]) / 2
    y = 400

    draw.text((x, y), text, font=font, fill='black')
    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="2-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type2.set()

@dp.message_handler(state=Type.type2)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/2-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 62)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = 160
    y = 350

    draw.text((x, y), text, font=font, fill='black')

    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="3-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type3.set()

@dp.message_handler(state=Type.type3)
async def satte_type3(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/3-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 62)
    text_size = draw.textbbox((120, 120), text, font=font)

    x = (img.width - text_size[2]) / 2
    y = 350

    draw.text((x, y), text, font=font, fill='white')

    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="4-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type4.set()

@dp.message_handler(state=Type.type4)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/4-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 62)
    text_size = draw.textbbox((120, 120), text, font=font)

    x = (img.width - text_size[2]) / 2
    y = 350

    draw.text((x, y), text, font=font, fill='black')

    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="5-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type5.set()

@dp.message_handler(state=Type.type5)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/5-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 62)
    text_size = draw.textbbox((120, 120), text, font=font)

    x = (img.width - text_size[2]) / 2
    y = 720

    draw.text((x, y), text, font=font, fill='black')

    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="6-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type6.set()

@dp.message_handler(state=Type.type6)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/6-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((120, 120), text, font=font)

    x = 110
    y = 230

    draw.text((x, y), text, font=font, fill='black')
    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="7-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type7.set()

@dp.message_handler(state=Type.type7)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/7-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((120, 120), text, font=font)

    x = 350
    y = 350

    draw.text((x, y), text, font=font, fill='black')
    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="8-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type8.set()

@dp.message_handler(state=Type.type8)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/8-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((120, 120), text, font=font)

    x = 1200
    y = 600

    draw.text((x, y), text, font=font, fill='black')
    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="9-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type9.set()

@dp.message_handler(state=Type.type9)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/9-type.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 24)
    text_size = draw.textbbox((120, 120), text, font=font)

    x = 250
    y = 370

    draw.text((x, y), text, font=font, fill='black')
    img.save("media/results.jpg")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
          "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/protabrikbot"
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()