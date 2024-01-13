from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from states.change_parametr import Change_States

from loader import db, dp, bot


from .callback_data import change_my_card_parametr


accept_button_yes = InlineKeyboardButton(
    text='Да', callback_data="accept_button_yes")
accept_button_no = InlineKeyboardButton(
    text='Нет', callback_data="accept_button_no")
accept_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(
    accept_button_yes, accept_button_no)

### Изменить ###
button1 = InlineKeyboardButton(text='Изменить', callback_data='change_my_card')
change_my_card = InlineKeyboardMarkup().add(button1)

### Параметры ###


@dp.callback_query_handler(text='change_my_card')
async def select_parametr(call: types.CallbackQuery, state: FSMContext):
    # await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    sql = "SELECT * FROM lst_oper WHERE type = %s;"
    result = db.execute(sql, parameters=('user',), fetchall=True)
    change_card = InlineKeyboardMarkup(row_width=3)
    for x in result:
        change_card.add(InlineKeyboardButton(
            text=x[1], callback_data=change_my_card_parametr.new(paramepr=x[0], name=x[1])))
    await call.message.answer("Выберите параметр:", reply_markup=change_card)


@dp.callback_query_handler(change_my_card_parametr.filter())
async def change_parametr_0(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    quantity = callback_data.get('paramepr')
    name = callback_data.get('name')
    await state.update_data({'parametr': quantity})
    await call.message.answer(f"Введите {name.lower()}")
    await Change_States.STATE_1.set()


@dp.message_handler(state=Change_States.STATE_1)
async def change_parametr_1(message: types.Message, state: FSMContext):
    await state.update_data({'value': message.text})
    await message.answer("Вы действительно хотите изменить параметр?", reply_markup=accept_keyboard)
    await Change_States.next()
