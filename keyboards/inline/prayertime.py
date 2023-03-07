from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

answer_to_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Javob yozish", callback_data='javobyozish')
        ]
    ]
)