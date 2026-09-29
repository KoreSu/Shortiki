import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message


f = int(input(""))


tg_bot_token = "ТОКЕН вашего телеграм бота"

dp = Dispatcher()

@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет! Это первое сообщение бота! Оно высвечивается, когда пользователь вводит команду /start")

@dp.message(F.text=="/donation")
async def command_start(message: Message) -> None:
    await message.answer("Поддержать автора можно здесь{f}")

@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет!")




async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())