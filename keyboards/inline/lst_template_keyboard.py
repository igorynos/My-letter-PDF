from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

from loader import db, dp


from .callback_data import lst_template_callback


### Шаблоны ###

async def lst_template_keyboard(message: types.Message):
    sql = "SELECT * FROM template"
    result = db.execute(sql, fetchall=True)

    change_card = InlineKeyboardMarkup(row_width=3)
    for x in result:
        change_card.add(InlineKeyboardButton(
            text=x[1], callback_data=lst_template_callback.new(id=x[0])))
    change_card.add(InlineKeyboardButton(
        "➕ Добавить шаблон", callback_data='add_new_tеmplate'))
    await message.answer("Шаблоны:", reply_markup=change_card)

### Изменить ###

button1 = InlineKeyboardButton(
    text='Изменить ссылку', callback_data='change_template')
button2 = InlineKeyboardButton(
    text='Удалить шаблон', callback_data='delete_template')
change_template = InlineKeyboardMarkup().add(button1, button2)
