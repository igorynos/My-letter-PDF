from loader import dp, db, bot
from aiogram import types
from aiogram.dispatcher.storage import FSMContext


from keyboards.inline.change_my_card import change_my_card
from keyboards.default.main_menu import main_menu
from states.change_parametr import Change_States


@dp.message_handler(text='Мои реквизиты')
async def my_card(message: types.Message):
    sql = "SELECT * FROM users WHERE id = %s;"
    result = db.execute(sql, parameters=(message.chat.id,), fetchall=True)
    result = result[0]

    text = f"#myinfo (@{message.chat.username})\n\n\
{result[1]}\n\
Адрес: {result[2]}\n\
Тел: {result[3]}\n\
Email: {result[4]}\n\
ИНН: {result[5]}\n\
Паспорт: {result[6]}\n\
Дата рождения: {result[7]}\n\
Комментарий: {result[8]}"
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=change_my_card)

# change my card ### final state


@dp.callback_query_handler(state=Change_States.CONFIRMATION)
async def change_parametr_2(call: types.CallbackQuery, state: FSMContext):
    if call.data == "accept_button_yes":
        data = await state.get_data()
        db.update_user(id=call.message.chat.id, dict_oper={
                       data['parametr']: data['value']})
        sql = "SELECT shot FROM lst_oper WHERE oper = %s;"
        result = db.execute(sql, parameters=(data['parametr'],), fetchone=True)
        await call.message.answer(f"{result[0]} изменён", reply_markup=main_menu(call.message))
        await my_card(call.message)
    elif call.data == "accept_button_no":
        data = await state.get_data()
        sql = "SELECT shot FROM lst_oper WHERE oper = %s;"
        result = db.execute(sql, parameters=(data['parametr'],), fetchone=True)
        await call.message.answer(f"{result[0]} не изменён", reply_markup=main_menu(call.message))
        await my_card(call.message)
    await state.finish()
