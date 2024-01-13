from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext

from loader import dp, db

from .register_new_user import register_new
from keyboards.default.main_menu import main_menu
from .show_my_card import my_card


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    sql = f"SELECT * FROM users WHERE id = '{message.chat.id}';"
    result = db.execute(sql, fetchone=True)
    if result is None:
        await register_new(message, state)
    await message.answer("Ваши реквизиты:", reply_markup=main_menu(message))
    await my_card(message)
