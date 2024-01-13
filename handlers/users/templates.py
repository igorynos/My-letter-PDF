from loader import dp, db, bot
from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from keyboards.default.main_menu import main_menu
from keyboards.inline.lst_template_keyboard import lst_template_keyboard, change_template
from keyboards.inline.callback_data import lst_template_callback


import random

dict_template_id = {}


@dp.message_handler(text='Шаблоны')
async def lst_tamplate(message: types.Message):
    await lst_template_keyboard(message)


@dp.callback_query_handler(text='delete_template')
async def dell_tamplate(call: types.CallbackQuery):
    db.delete_template(id=dict_template_id[f"{call.message.chat.id}"])
    await call.message.answer("Шаблон удалён")
    await lst_template_keyboard(call.message)


@dp.callback_query_handler(text='change_template')
async def change_tamplate(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Вставьте ссылку на шаблон в Google docs")
    await call.message.answer("В формате 'https://docs.google.com/document/пример/пример/edit'")
    await call.message.answer("Откройте доступ к файлу")
    await state.set_state("change_link")


@dp.callback_query_handler(text='add_new_tеmplate')
async def add_new_tеmplate(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Напиши название шаблона")
    await state.set_state('name_tamplate')


@dp.message_handler(state="name_tamplate")
async def name_acc(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {
            'name': name
        }
    )
    await message.answer("Вставьте ссылку на шаблон в Google docs")
    await message.answer("В формате 'https://docs.google.com/document/пример/пример/edit'")
    await message.answer("Откройте доступ к файлу")
    await state.set_state("link_template")


@dp.message_handler(state="link_template")
async def link_template(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    link_template = message.text
    link_template = link_template.replace("/edit", "/export?format=docx")

    db.add_template(name=name, link=link_template,
                    template_id=random.randint(1000000, 9999999))

    await state.finish()

    await message.answer(text=f'Новый шаблон {name} создан', reply_markup=await lst_template_keyboard(message))


@dp.message_handler(state="change_link")
async def link_template(message: types.Message, state: FSMContext):
    link_template = message.text
    link_template = link_template.replace("/edit", "/export?format=docx")
    template_id = dict_template_id[f"{message.chat.id}"]
    db.update_template(link=link_template,
                       id=template_id)

    await state.finish()

    await message.answer(text=f'Шаблон изменён', reply_markup=await lst_template_keyboard(message))


@dp.callback_query_handler(lst_template_callback.filter())
async def cont_users_card(call: types.CallbackQuery, callback_data: dict):
    cont_id = callback_data.get("id")
    sql = "SELECT * FROM template WHERE id = %s;"
    result = db.execute(sql, parameters=(cont_id,), fetchall=True)
    result = result[0]
    dict_template_id[f"{call.message.chat.id}"] = cont_id
    link_template = result[2].replace("/export?format=docx", "/edit")

    text = f"Шаблон {result[1]}\n\
ссылка:\n\
{link_template}"
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=change_template)
