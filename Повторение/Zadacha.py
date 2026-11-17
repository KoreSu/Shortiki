import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import BotCommand
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from dotenv import load_dotenv
import os
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboard2 import main_menu_keyboard
from keyboard2 import math_keyboard
from keyboard2 import back_keyboard

load_dotenv()

dp = Dispatcher(storage=MemoryStorage())

tg_bot_token = os.getenv("TG_BOT_TOKEN")

class States(StatesGroup):
    waiting_number_one = State()
    waiting_number_two = State()


async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)





@dp.message(F.text=="/start")
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в бота", reply_markup=main_menu_keyboard)

@dp.message(F.text=='Подменю_1')
async def button_one(message: Message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer("Зафиксировано нажатие на кнопку Подменю_1", reply_markup=math_keyboard)

@dp.message(F.text=='Сложить')
async def start_command(message: Message, state: FSMContext):

    await message.answer("Введите число")

    await state.set_state(States.waiting_number_one)

@dp.message(States.waiting_number_one)
async def process_name(message: Message, state: FSMContext):

    await message.answer(f"Введите 2 число")

    await state.set_state(States.waiting_number_two)

    await state.update_data(first=message.text)

@dp.message(States.waiting_number_two)
async def process_age(message: Message, state: FSMContext):

    temp_data = await state.get_data()
    print(temp_data["first"])

    await message.answer(f"{temp_data["first"]} + {message.text}")

    await state.clear()  

@dp.message(F.text=='Главное меню')
async def button_one(message: Message):
    await message.delete()
    await message.answer("Главное меню",reply_markup=main_menu_keyboard)

if __name__ == "__main__":
    asyncio.run(main())















@dp.message(F.text=='*')
async def button_one(message: Message):
    await message.delete()
    await message.answer("Текст кнопки *")

@dp.message(F.text=='-')
async def button_one(message: Message):
    await message.delete()
    await message.answer("Текст кнопки -")

@dp.message(F.text=='Главное меню')
async def button_one(message: Message):
    await message.delete()
    await message.answer("Главное меню",reply_markup=main_menu_keyboard)