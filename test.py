import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import BotCommand
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
dp = Dispatcher()

tg_bot_token = "8703457324:AAF73WOjeXwtQ_yA7luPR6TNdF8VoD7Uwqs"

async def set_commands_menu(bot):
    bot_commands = [
        BotCommand(command="/start", description="Запуск!"),
    ]
    await bot.set_my_commands(bot_commands)

async def main():
    bot = Bot(token=tg_bot_token)

    await set_commands_menu(bot)

    await dp.start_polling(bot)

@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет!")

if __name__ == "__main__":
    asyncio.run(main())