from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Хочу записаться на разговорный клуб'),
            KeyboardButton(text=' Получить бесплатный чек-лист для подготовки к экзаменам')
        ],
        [
            KeyboardButton(text='Скачать колесо языкового баланса'),
            KeyboardButton(text='Хочу посмотреть презентацию к лекции "Do you speak English? yess..ли бы"')
        ],
        [
            KeyboardButton(text='Узнать свой уровень английского'),
            KeyboardButton(text='Записаться ко мне на занятие')
        ],
    ]
)