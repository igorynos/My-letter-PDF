from loader import dp, db, bot
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.inline.lst_cont_user import lst_cont_users_keyboard
from keyboards.default.main_menu import main_menu

from states import Add_new_cont_user_state

import random

from handlers.users.dadata_api import dadata_start, dadata_check

Dict_temp_oper = {}
Dict_turn = {}


pass_parametr = KeyboardButton(
    text='Пропустить')
pass_parametr_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True).add(pass_parametr)


def inn_to_start(lst):
    my_list = lst
    element_to_move = None
    for x in lst:
        if 'cont_inn' in x:
            element_to_move = x

    index_of_element = my_list.index(element_to_move)

    my_list.pop(index_of_element)

    my_list.insert(0, element_to_move)

    return my_list


@dp.callback_query_handler(text="add_new_cont_user")
async def add_new_cont_user(call: types.CallbackQuery, state: FSMContext):
    sql = "SELECT * FROM lst_oper WHERE type = %s;"
    result = db.execute(sql, parameters=('cont_user',), fetchall=True)
    Dict_temp_oper[f'{call.message.chat.id}'] = inn_to_start(list(result))
    Dict_turn[f'{call.message.chat.id}'] = 0

    await call.message.answer("Напиши ИНН получателя")
    await Add_new_cont_user_state.first()


@dp.message_handler(state=Add_new_cont_user_state.Q0)
async def register_0(message: types.Message, state: FSMContext):
    value = message.text

    cont_id = random.randint(1000000, 9999999)

    await state.update_data({'cont_id': cont_id})

    db.add_cont_user(cont_id=cont_id, cont_inn=value,
                     cont_user=message.chat.id)

    Dict_turn[f'{message.chat.id}'] += 1

    if dadata_check(value):
        Dict_temp_oper[f'{message.chat.id}'] = dadata_start(cont_id, value)
        Dict_turn[f'{message.chat.id}'] -= 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]
        if result[3] == 'Наименование организации получателя':
            await message.answer(f"Напиши {result[3].lower()}")
        else:
            await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        await state.finish()


@dp.message_handler(state=Add_new_cont_user_state.Q1)
async def register_1(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q2)
async def register_2(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q3)
async def register_3(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q4)
async def register_4(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q5)
async def register_5(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q6)
async def register_6(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q7)
async def register_7(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q8)
async def register_8(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q9)
async def register_9(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q10)
async def register_10(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q11)
async def register_11(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)


@dp.message_handler(state=Add_new_cont_user_state.Q12)
async def register_12(message: types.Message, state: FSMContext):
    value = message.text
    result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

    data = await state.get_data()
    cont_id = data["cont_id"]

    await state.update_data({f'{result[0]}': f'{value}'})

    Dict_turn[f'{message.chat.id}'] += 1

    try:
        result = Dict_temp_oper[f'{message.chat.id}'][Dict_turn[f'{message.chat.id}']]

        await message.answer(f"Напиши {result[3].lower()}", reply_markup=pass_parametr_keyboard)
        await Add_new_cont_user_state.next()

    except:
        data = await state.get_data()
        db.update_cont_user(cont_id, dict_oper=data)
        await state.finish()
        await message.answer(f"Получатель добавлен", reply_markup=main_menu(message))
        await lst_cont_users_keyboard(message)
