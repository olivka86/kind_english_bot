from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

assign_to = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Записаться сейчас'),
            KeyboardButton(text='Расскажи о себе')
        ],
        [
            KeyboardButton(text='Покажи отзывы'),
            KeyboardButton(text='Сколько стоит занятие?')
        ],
    ]
)

assign_just_now = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Записаться сейчас")]]
)
