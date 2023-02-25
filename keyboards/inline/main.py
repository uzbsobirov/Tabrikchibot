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

def range_numbers():
    numbers = InlineKeyboardMarkup(row_width=3)
    for number in range(1, 10):
        numbers.insert(
            InlineKeyboardButton(
                text=number,
                callback_data=f'{number}-type'
            )
        )
    numbers.insert(
        InlineKeyboardButton(
            text="◀️ Orqaga",
            callback_data='back'
        )
    )
    return numbers

def share(url):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(
        InlineKeyboardButton(
            text="⤴️ Do'stlarga ulashish",
            url=url
        )
    )
    return markup