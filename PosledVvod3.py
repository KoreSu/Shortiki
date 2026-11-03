import random
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import BotCommand
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from dotenv import load_dotenv
import os
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

load_dotenv()
dp = Dispatcher(storage=MemoryStorage())


tg_bot_token = os.getenv("TG_BOT_TOKEN")

class States(StatesGroup):
    waiting_number_one = State()
    waiting_number_two = State()
    waiting_number_three = State()



@dp.message(F.text=="/Random")
async def start_command(message: Message, state: FSMContext):

    await message.answer(f"Введите 1 число:")
    await state.set_state(States.waiting_number_one)



@dp.message(States.waiting_number_one)
async def process_name(message: Message, state: FSMContext):
    await message.answer(f"Введите 2 число:")
    await state.set_state(States.waiting_number_two)
    await state.update_data(number_one=message.text)



@dp.message(States.waiting_number_two)
async def process_name(message: Message, state: FSMContext):
    await message.answer(f"Введите 3 число:")
    await state.set_state(States.waiting_number_three)
    await state.update_data(number_two=message.text)



@dp.message(States.waiting_number_three)
async def process_name(message: Message, state: FSMContext):


    temp_data = await state.get_data()
    number_one = temp_data["number_one"]
    number_two = temp_data["number_two"]
    number_three = message.text

    lucky = random.choice(["number_one", "number_two", "number_three"])
    await message.answer(f"Счастливо число:{lucky}")
    
    await state.clear()  






# @dp.message(States.waiting_name)
# async def process_name(message: Message, state: FSMContext):

#     await message.answer(f"Введите имя друга")
#     await state.set_state(States.waiting_friend_name)
#     await state.update_data(name=message.text)
