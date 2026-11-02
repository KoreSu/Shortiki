import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import BotCommand
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
import os

load_dotenv()
dp = Dispatcher(storage=MemoryStorage())


tg_bot_token = os.getenv("TG_BOT_TOKEN")

class States(StatesGroup):
    waiting_name = State()
    waiting_friend_name = State()
    waiting_age = State()

async def set_commands_menu(bot):
    bot_commands = [
        BotCommand(command="/start", description="Запуск!"),
    ]
    await bot.set_my_commands(bot_commands)



async def main():
    bot = Bot(token=tg_bot_token)

    await set_commands_menu(bot)

    await dp.start_polling(bot)

# ---------------------

@dp.message(F.text=='/friend')
async def start_command(message: Message, state: FSMContext):

    await message.answer("Введите имя")
    await state.set_state(States.waiting_name)
    await state.update_data(name=message.text)

@dp.message(States.waiting_friend_one)
async def process_name(message: Message, state: FSMContext):

    await message.answer(f"Введите имя друга")

    await state.set_state(States.waiting_friend_name)


@dp.message(States.waiting_friend_one)
async def process_name(message: Message, state: FSMContext):

    await message.answer(f"Сколько лет вы дружите?")
    await state.update_data(friend_name=message.text)
    await state.set_state(States.waiting_age)



@dp.message(States.waiting_age)
async def process_age(message: Message, state: FSMContext):

    temp_data = await state.get_data()

    age = message.text

    await message.answer(f"{temp_data["first"]} + {message.text}")

    await state.clear()  

# --------------------

@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет!")

if __name__ == "__main__":
    asyncio.run(main())

