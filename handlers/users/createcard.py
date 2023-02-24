from PIL import Image, ImageDraw, ImageFont

from keyboards.inline.main import range_numbers
from loader import dp, db, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.one import Type
@dp.callback_query_handler(text="createcard", state='*')
async def create_card(call: types.CallbackQuery, state: FSMContext):

    # Photo urls
    photo1_url = 'https://t.me/forchrabot/55'
    photo2_url = 'https://t.me/forchrabot/56'
    photo3_url = 'https://t.me/forchrabot/57'
    photo4_url = 'https://t.me/forchrabot/60'

    await call.message.answer_photo(photo=photo1_url, caption="Keraklisini tanlang: ", reply_markup=range_numbers())


@dp.callback_query_handler(text="1-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Ism kiriting...")
    await Type.type1.set()

@dp.message_handler(state=Type.type1)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    # gfg_logo.jpeg image opened using open function and
    # assigned to variable named img
    img = Image.open('media/1-type.jpg')

    # Image is converted into editable form using Draw
    # function and assigned to d1
    d1 = ImageDraw.Draw(img)

    # Decide the text location, color and font
    d1.text((600, 350), text, fill =(50, 255, 100))

    # show and save the image
    # img.show()
    img.save("media/results.jpg")
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption='Ol ino')
        await state.finish()

@dp.callback_query_handler(text="2-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Ism kiriting...")
    await Type.type2.set()

@dp.message_handler(state=Type.type2)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    # gfg_logo.jpeg image opened using open function and
    # assigned to variable named img
    img = Image.open('media/2-type.jpg')

    # Image is converted into editable form using Draw
    # function and assigned to d1
    d1 = ImageDraw.Draw(img)

    # Decide the text location, color and font
    d1.text((600, 350), text, fill =(50, 255, 100))

    # show and save the image
    # img.show()
    img.save("media/results.jpg")
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption='Ol ino')
        await state.finish()

@dp.callback_query_handler(text="3-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Ism kiriting...")
    await Type.type3.set()

@dp.message_handler(state=Type.type3)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    # gfg_logo.jpeg image opened using open function and
    # assigned to variable named img
    img = Image.open('media/3-type.jpg')

    # Image is converted into editable form using Draw
    # function and assigned to d1
    d1 = ImageDraw.Draw(img)

    # Decide the text location, color and font
    d1.text((600, 350), text, fill =(50, 255, 100))

    # show and save the image
    # img.show()
    img.save("media/results.jpg")
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption='Ol ino')
        await state.finish()

@dp.callback_query_handler(text="4-type")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Ism kiriting...")
    await Type.type4.set()

@dp.message_handler(state=Type.type4)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    # gfg_logo.jpeg image opened using open function and
    # assigned to variable named img
    img = Image.open('media/4-type.jpg')

    # Image is converted into editable form using Draw
    # function and assigned to d1
    d1 = ImageDraw.Draw(img)

    # Decide the text location, color and font
    d1.text((600, 350), text, fill =(50, 255, 100))

    # show and save the image
    # img.show()
    img.save("media/results.jpg")
    with open(file='media/results.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption='Ol ino')
        await state.finish()

# @dp.callback_query_handler(text="1-type")
# async def number_func(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     await call.message.answer(text="Ism kiriting...")
#     await Type.type1.set()
#
# @dp.message_handler(state=Type.type1)
# async def satte_type1(message: types.Message, state: FSMContext):
#     text = message.text
#
#     # gfg_logo.jpeg image opened using open function and
#     # assigned to variable named img
#     img = Image.open('media/1-type.jpg')
#
#     # Image is converted into editable form using Draw
#     # function and assigned to d1
#     d1 = ImageDraw.Draw(img)
#
#     # Decide the text location, color and font
#     d1.text((600, 350), text, fill =(50, 255, 100))
#
#     # show and save the image
#     # img.show()
#     img.save("media/results.jpg")
#     with open(file='media/results.jpg', mode='rb') as photo:
#         await message.answer_photo(photo=photo, caption='Ol ino')
#         await state.finish()

# @dp.callback_query_handler(text="1-type")
# async def number_func(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     await call.message.answer(text="Ism kiriting...")
#     await Type.type1.set()
#
# @dp.message_handler(state=Type.type1)
# async def satte_type1(message: types.Message, state: FSMContext):
#     text = message.text
#
#     # gfg_logo.jpeg image opened using open function and
#     # assigned to variable named img
#     img = Image.open('media/1-type.jpg')
#
#     # Image is converted into editable form using Draw
#     # function and assigned to d1
#     d1 = ImageDraw.Draw(img)
#
#     # Decide the text location, color and font
#     d1.text((600, 350), text, fill =(50, 255, 100))
#
#     # show and save the image
#     # img.show()
#     img.save("media/results.jpg")
#     with open(file='media/results.jpg', mode='rb') as photo:
#         await message.answer_photo(photo=photo, caption='Ol ino')
#         await state.finish()
#
# @dp.callback_query_handler(text="1-type")
# async def number_func(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     await call.message.answer(text="Ism kiriting...")
#     await Type.type1.set()
#
# @dp.message_handler(state=Type.type1)
# async def satte_type1(message: types.Message, state: FSMContext):
#     text = message.text
#
#     # gfg_logo.jpeg image opened using open function and
#     # assigned to variable named img
#     img = Image.open('media/1-type.jpg')
#
#     # Image is converted into editable form using Draw
#     # function and assigned to d1
#     d1 = ImageDraw.Draw(img)
#
#     # Decide the text location, color and font
#     d1.text((600, 350), text, fill =(50, 255, 100))
#
#     # show and save the image
#     # img.show()
#     img.save("media/results.jpg")
#     with open(file='media/results.jpg', mode='rb') as photo:
#         await message.answer_photo(photo=photo, caption='Ol ino')
#         await state.finish()
#


