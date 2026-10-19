from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📊 Математика'), KeyboardButton(text='✏️ Текст')],
],
resize_keyboard=True)

math_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=' + '), KeyboardButton(text=' - '), KeyboardButton(text=' * ')],
    [KeyboardButton(text=' Главное меню ')]
],
resize_keyboard=True)

back_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=' Главное меню ')]
],
resize_keyboard=True)