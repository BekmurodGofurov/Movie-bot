from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancle = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Bekor qilish ❌", callback_data="$cancel")
    ]
])

add_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ha albatta😀", callback_data="$add_movie")
    ],
    [
        InlineKeyboardButton(text="Hozir emas ❌", callback_data="$cancel")
    ]
])

start_001 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ha albatta😀", callback_data="$add_movie")
    ]
])

save_data = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ha albatta😀", callback_data="$save")
    ],
    [
        InlineKeyboardButton(text="Hoxlamayman ❌", callback_data="$cancel")
    ]
])

join = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Kanalga qoshilsih", url="https://t.me/tarjima_kinolaruz_1")
    ],
    [
        InlineKeyboardButton(text="Tasdiqlash", callback_data="$check")
    ]
])