
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подменю_1'), KeyboardButton(text='Подменю_2')],
    [KeyboardButton(text='СЛОЖИТЬ')]
],
resize_keyboard=True)

math_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подподменю1'), KeyboardButton(text='Подподменю2')]
    [KeyboardButton(text=' Главное меню ')]
],
resize_keyboard=True)

back_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=' Главное меню ')]
],
resize_keyboard=True)