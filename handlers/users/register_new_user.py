from loader import dp, db
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states import Register_new_user_state
from keyboards.default.main_menu import main_menu

Dict_temp_oper = {}
Dict_turn = {}

pass_parametr = KeyboardButton(
    text='Пропустить', callback_data="pass_parametr")
pass_parametr_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True).add(pass_parametr)


async def register_new(message: types.Message, state: FSMContext):
    sql = "SELECT * FROM lst_oper WHERE type = %s;"
    result = db.execute(sql, parameters=('user',), fetchall=True)
    Dict_temp_oper[f'{message.chat.id}'] = result
    Dict_turn[f'{message.chat.id}'] = 0

    await message.answer("Напиши своё ФИО")
    await Register_new_user_state.first()


async def handle_registration(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    await state.update_data({f'{result[0]}': f'{value}'})
    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]
        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Register_new_user_state.next()
    except:
        data = await state.get_data()
        db.add_user(id=message.chat.id, name=data['fio'])
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q0)
async def register_0(message: types.Message, state: FSMContext):
    await handle_registration(message, state)


@dp.message_handler(state=Register_new_user_state.Q1)
@dp.message_handler(state=Register_new_user_state.Q2)
@dp.message_handler(state=Register_new_user_state.Q3)
@dp.message_handler(state=Register_new_user_state.Q4)
@dp.message_handler(state=Register_new_user_state.Q5)
@dp.message_handler(state=Register_new_user_state.Q6)
@dp.message_handler(state=Register_new_user_state.Q7)
@dp.message_handler(state=Register_new_user_state.Q8)
@dp.message_handler(state=Register_new_user_state.Q9)
@dp.message_handler(state=Register_new_user_state.Q10)
@dp.message_handler(state=Register_new_user_state.Q11)
@dp.message_handler(state=Register_new_user_state.Q12)
@dp.message_handler(state=Register_new_user_state.Q13)
@dp.message_handler(state=Register_new_user_state.Q14)
@dp.message_handler(state=Register_new_user_state.Q15)
@dp.message_handler(state=Register_new_user_state.Q16)
@dp.message_handler(state=Register_new_user_state.Q17)
@dp.message_handler(state=Register_new_user_state.Q18)
@dp.message_handler(state=Register_new_user_state.Q19)
async def handle_registration_questions(message: types.Message, state: FSMContext):
    await handle_registration(message, state)
