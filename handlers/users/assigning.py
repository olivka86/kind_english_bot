from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from aiogram import types
from states import Test
from keyboards import assign_to


@dp.message_handler(text="Записаться ко мне на занятие", state=None)
async def enter_assign(message: types.Message):
    await message.answer(text="Хорошо", reply_markup=assign_to)
    await Test.first()


@dp.message_handler(text="Записаться сейчас")
async def answer_q1(message: types.Message):
    await message.answer(text="Здесь можно записаться\ngoogle.com ", reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(state=Test.Q2)
# async def answer_q2(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     answer1 = data.get("answer1")
#     answer2 = message.text
#
#     await message.answer("Вы записаны на занятие")
#     await message.answer(f"Ответ 1:{answer1}")
#     await message.answer(f"Ответ 2:{answer2}")
#
#     await state.reset_state()
