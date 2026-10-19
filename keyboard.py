from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from aiogram.types import BotCommand
import random


main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📊 Математика'), KeyboardButton(text='✏️ Текст')],
],
resize_keyboard=True)

