from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

from loader import db, dp


from .callback_data import lst_cont_user_callback
### Получатели ###


async def lst_cont_users_keyboard(message: types.Message):
    sql = "SELECT * FROM cont_users WHERE cont_user = %s;"
    result = db.execute(sql, parameters=(message.chat.id,), fetchall=True)

    change_card = InlineKeyboardMarkup(row_width=3)
    for x in result:
        change_card.add(InlineKeyboardButton(
            text=x[2], callback_data=lst_cont_user_callback.new(cont_id=x[0])))
    change_card.add(InlineKeyboardButton(
        "➕ Добавить получателя", callback_data='add_new_cont_user'))
    await message.answer("Получатели:", reply_markup=change_card)
