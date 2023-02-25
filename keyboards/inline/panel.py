from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Statistika", callback_data='statistika'),
            InlineKeyboardButton(text="🗞 Reklama yuborish", callback_data='reklama')
        ],
        [
            InlineKeyboardButton(text="📢 Majburiy obuna", callback_data='majburiy')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='orqaga')
        ]
    ]
)

back = InlineKeyboardMarkup(row_width=1)
back.insert(InlineKeyboardButton(text="◀️ Orqaga", callback_data='orqaga'))


typesads = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🖼 Image", callback_data='image')],
        [InlineKeyboardButton(text="📹 Video", callback_data='video')],
        [InlineKeyboardButton(text="✍️ Text", callback_data='text')],
        [InlineKeyboardButton(text="🗂 MediaGroup", callback_data="mediagroup")],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='orqaga')
        ]
    ]
)

add_sponsor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Kanal qo'shish", callback_data='addsponsor')
        ],
        [
            InlineKeyboardButton(text="🗑 Kanalni o'chirish", callback_data='deletesponsor')
        ],
[
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='orqaga')
        ]
    ]
)

sponsor_add = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Yana qo'shish", callback_data='addsponsor')
        ]
    ]
)