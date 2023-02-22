from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌸 Tabrik yasash",
                callback_data='createcard'
            )
        ]
    ]
)