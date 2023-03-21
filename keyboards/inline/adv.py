from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

types_private = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖼 Surat", callback_data='withpictureprivate'),
            InlineKeyboardButton(text="📹 Video", callback_data='withvideoprivate')
        ],
        [
            InlineKeyboardButton(text="📝 Text", callback_data='withtextprivate')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='stat_back')
        ]
    ]
)


yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Ha", callback_data='choose_ha')
        ],
        [
            InlineKeyboardButton(text="❌ Yo'q", callback_data='choose_yoq')
        ]
    ]
)


def buttons(text, url):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(
        InlineKeyboardButton(text=text, url=url)
    )
    return markup


back_privatee = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back_private_adv')
        ]
    ]
)