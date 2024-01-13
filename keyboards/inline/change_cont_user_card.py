from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from states.change_parametr import Change_States_cont_user

from loader import db, dp


from .callback_data import change_cont_parametr


accept_button_yes = InlineKeyboardButton(
    text='Да', callback_data="accept_button_yes")
accept_button_no = InlineKeyboardButton(
    text='Нет', callback_data="accept_button_no")
accept_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(
    accept_button_yes, accept_button_no)

accept_dell_yes = InlineKeyboardButton(
    text='Да', callback_data="accept_dell_yes")
accept_dell_no = InlineKeyboardButton(
    text='Нет', callback_data="accept_dell_no")
dell_cont_user = InlineKeyboardMarkup(resize_keyboard=True).add(
    accept_dell_yes, accept_dell_no)

### Изменить ###
button1 = InlineKeyboardButton(
    text='Изменить', callback_data='change_cont_user')
button2 = InlineKeyboardButton(
    text='Удалить', callback_data='delete_cont_user')
change_cont_user_card = InlineKeyboardMarkup().add(button1, button2)

### Параметры ###


@dp.callback_query_handler(text='change_cont_user')
async def select_parametr_cont_user(call: types.CallbackQuery, state: FSMContext):
    sql = "SELECT * FROM lst_oper WHERE type = %s;"
    result = db.execute(sql, parameters=('cont_user',), fetchall=True)
    change_card = InlineKeyboardMarkup(row_width=3)
    for x in result:
        change_card.add(InlineKeyboardButton(
            text=x[1], callback_data=change_cont_parametr.new(paramepr=x[0], name=x[1])))
    await call.message.answer("Выберите параметр:", reply_markup=change_card)


@dp.callback_query_handler(change_cont_parametr.filter())
async def change_parametr_0_cont_user(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    quantity = callback_data.get('paramepr')
    name = callback_data.get('name')
    await state.update_data({'parametr': quantity})
    await call.message.answer(f"Введите {name.lower()}")
    await Change_States_cont_user.STATE_1.set()


@dp.message_handler(state=Change_States_cont_user.STATE_1)
async def change_parametr_1_cont_user(message: types.Message, state: FSMContext):
    await state.update_data({'value': message.text})
    await message.answer("Вы действительно хотите изменить параметр?", reply_markup=accept_keyboard)
    await Change_States_cont_user.CONFIRMATION.set()
