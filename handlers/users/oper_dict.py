from loader import dp, db
from aiogram import types
from keyboards.default.main_menu import main_menu


@dp.message_handler(text='Словарь операндов')
async def dict_oper(message: types.Message):
    text = "{{fio}} - имя пользователя\n\
{{adress}} - адрес отправителя\n\
{{phone}} - ваш номер телефона\n\
{{email}} - email пользователя\n\
{{inn}} - ИНН пользователя\n\
{{pasport}} - пасспорт пользователя\n\
{{born}} - дату рождения пользователя\n\
{{comment}} - комментарий пользователя\n\
{{cont_org}} - наименование организации получателя\n\
{{cont_ogrn}} - ОГРН организации получателя\n\
{{cont_adress}} - почтовый адрес организации получателя'\n\
{{cont_phone}} - телефон представителя организации получателя'\n\
{{cont_email}} - Email организации получателя'\n\
{{cont_inn}} - ИНН организации получателя\n\
{{cont_comment}} - комментарий (статус) организации получателя\n\
{{cont_fio}} - ФИО руководителя организации получателя\n\
{{cont_headstatus}} - должность руководителя организации получателя\n\
{{cont_fiocont}} - ФИО представителя организации получателя\n\
{{cont_link}} - ссылка на организацию получателя\n\
{{doc_text}} - дополнительный текст"
    await message.answer(text=text, reply_markup=main_menu(message))
