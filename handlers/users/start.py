from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from utils.misc import rate_limit
from keyboards import menu


@rate_limit(5)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Тебя приветсвует добрый english bot', reply_markup=menu)

