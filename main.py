import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import BotCommand
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from keyboard import main_menu_keyboard



tg_bot_token = "8703457324:AAF73WOjeXwtQ_yA7luPR6TNdF8VoD7Uwqs"

dp = Dispatcher()


async def set_commands_menu(bot):
    bot_commands = [
        BotCommand(command="/start", description="Запуск!"),
        BotCommand(command="/help", description="Получить справку по работе с ботом"),
        BotCommand(command="/donat", description="Поддержать автора"),
        BotCommand(command="/random", description="Рандомное имя"),
        BotCommand(command="/random_number", description="Рандомное число"),
        BotCommand(command="/better", description="Бот выберет большее число из 2 введеных")
    ]
    await bot.set_my_commands(bot_commands)

async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)


async def main():
    bot = Bot(token=tg_bot_token)

    await set_commands_menu(bot)

    await dp.start_polling(bot)

from aiogram.types import Message

@dp.message(F.text=="/start")
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в бота", reply_markup=main_menu_keyboard)

@dp.message(F.text=='📊 Математика')
async def button_one(message: Message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer("Зафиксировано нажатие на кнопку Математика")

@dp.message(F.text=="/donat")
async def command_start(message: Message) -> None:
    await message.answer("Поддержать автора можно здесь{f}")

@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет!")

@dp.message(F.text=="/help")
async def command_start(message: Message) -> None:
    await message.answer("Поддержка не отвечает")

@dp.message(F.text.startswith("/better"))
async def command_start(message: Message) -> None:
    splited_message_text = message.text.split(" ")
    number1 = int(splited_message_text[1])
    number2 = int(splited_message_text[2])
    if number1 > number2:
        await message.answer(str(number1))
    else: await message.answer(str(number2))


spisok = ["Леха", "Зитракс", " Меганайт", "Улитки"]
@dp.message(F.text=="/random")
async def command_start(message: Message) -> None:
    await message.answer(random.choice(spisok))


@dp.message(F.text=="/random_number")
async def command_start(message: Message) -> None:
    await message.answer(str(random.randint(0,10)))

@dp.message(F.text.startswith("Мой возраст"))
async def command_start(message: Message) -> None:
    print("Мы(Я)")
    splited_message_text = message.text.split(" ")
    age = int(splited_message_text[2])
    await message.answer(f"Классно! А через 10 лет тебе будет {age + 10} лет")


if __name__ == "__main__":
    asyncio.run(main())

