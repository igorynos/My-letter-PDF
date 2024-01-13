from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db, dp

from data.config import ADMINS


def main_menu(message):
    main_menu_button_1 = KeyboardButton(
        text='Мои реквизиты')
    main_menu_button_2 = KeyboardButton(
        text='Получатели')
    main_menu_button_3 = KeyboardButton(
        text='Шаблоны')
    main_menu_button_4 = KeyboardButton(
        text='Словарь операндов')
    main_menu_button_5 = KeyboardButton(
        text='Создать письмо')
    main_menu_keyboard_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu_button_5).add(
        main_menu_button_1, main_menu_button_2).add(
        main_menu_button_3, main_menu_button_4)
    main_menu_keyboard_user = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu_button_5).add(
        main_menu_button_1, main_menu_button_2)
    if str(message.chat.id) in ADMINS:
        return main_menu_keyboard_admin
    else:
        return main_menu_keyboard_user
