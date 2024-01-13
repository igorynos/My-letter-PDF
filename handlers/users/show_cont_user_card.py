from loader import dp, db, bot
from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from keyboards.inline.lst_cont_user import lst_cont_users_keyboard
from keyboards.inline.change_cont_user_card import dell_cont_user
from keyboards.inline.callback_data import lst_cont_user_callback
from keyboards.inline.change_cont_user_card import change_cont_user_card
from keyboards.default.main_menu import main_menu
from states.change_parametr import Change_States_cont_user


dict_id_cont_user = {}


def result_cont(id):
    sql = "SELECT * FROM cont_users WHERE cont_id = %s;"
    result = db.execute(sql, parameters=(
        id,), fetchall=True)
    return result[0]


@dp.message_handler(text='Получатели')
async def lst_cont_users(message: types.Message):
    await lst_cont_users_keyboard(message)


@dp.callback_query_handler(text='delete_cont_user')
async def delete_cont_user(call: types.CallbackQuery, state: FSMContext):
    result = result_cont(dict_id_cont_user[f'{call.message.chat.id}'])
    await call.message.answer(f"Вы действительно хотите удалить {result[2]}?", reply_markup=dell_cont_user)


@dp.callback_query_handler(text='accept_dell_yes')
async def delete_cont_user_yes(call: types.CallbackQuery):
    result = result_cont(dict_id_cont_user[f'{call.message.chat.id}'])
    db.delete_cont_user(cont_id=dict_id_cont_user[f'{call.message.chat.id}'])
    await call.message.answer(f"Получатель {result[2]} удалён", reply_markup=await lst_cont_users_keyboard(call.message))


@dp.callback_query_handler(text='accept_dell_no')
async def delete_cont_user_no(call: types.CallbackQuery):
    await lst_cont_users_keyboard(call.message)


@dp.callback_query_handler(lst_cont_user_callback.filter())
async def cont_users_card(call: types.CallbackQuery, callback_data: dict):
    cont_id = callback_data.get("cont_id")
    sql = "SELECT * FROM cont_users WHERE cont_id = %s;"
    result = db.execute(sql, parameters=(cont_id,), fetchall=True)
    result = result[0]
    dict_id_cont_user[f'{call.message.chat.id}'] = cont_id

    text = f"#{result[7]}\n\
{result[2]} (ОГРН: {result[3]})\n\
Адрес: {result[4]}\n\
Получатель: {result[10]} - {result[9]}\n\
Представитель: {result[11]}\n\
Тел: {result[5]}\n\
Email: {result[6]}\n\
Ссылка: {result[12]}"
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=change_cont_user_card)


@dp.callback_query_handler(state=Change_States_cont_user.CONFIRMATION)
async def change_parametr_2_cont_user(call: types.CallbackQuery, state: FSMContext):
    if call.data == "accept_button_yes":
        data = await state.get_data()
        db.update_cont_user(cont_id=dict_id_cont_user[f'{call.message.chat.id}'], dict_oper={
            data['parametr']: data['value']})
        sql = "SELECT shot FROM lst_oper WHERE oper = %s;"
        result = db.execute(sql, parameters=(data['parametr'],), fetchone=True)
        await call.message.answer(f"{result[0]} изменён", reply_markup=main_menu(call.message))
        await state.finish()
        cont_id = {'cont_id': dict_id_cont_user[f'{call.message.chat.id}']}
        await cont_users_card(call=call, callback_data=cont_id)

    elif call.data == "accept_button_no":
        data = await state.get_data()
        sql = "SELECT shot FROM lst_oper WHERE oper = %s;"
        result = db.execute(sql, parameters=(data['parametr'],), fetchone=True)
        await call.message.answer(f"{result[0]} не изменён", reply_markup=main_menu(call.message))
        await state.finish()
        cont_id = {'cont_id': dict_id_cont_user[f'{call.message.chat.id}']}
        await cont_users_card(call=call, callback_data=cont_id)
