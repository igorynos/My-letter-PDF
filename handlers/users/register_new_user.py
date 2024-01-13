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


@dp.message_handler(state=Register_new_user_state.Q0)
async def register_0(message: types.Message, state: FSMContext):
    value = message.text

    db.add_user(name=value, id=message.chat.id)
    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Register_new_user_state.next()

    except:
        await state.finish()


@dp.message_handler(state=Register_new_user_state.Q1)
async def register_1(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q2)
async def register_2(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q3)
async def register_3(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q4)
async def register_4(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q5)
async def register_5(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q6)
async def register_6(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q7)
async def register_7(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q8)
async def register_8(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))


@dp.message_handler(state=Register_new_user_state.Q9)
async def register_9(message: types.Message, state: FSMContext):
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
        db.update_user(id=message.chat.id, dict_oper=data)
        await state.finish()
        await message.answer(f"Данные добавленны", reply_markup=main_menu(message))
