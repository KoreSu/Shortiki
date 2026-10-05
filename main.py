import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import BotCommand


tg_bot_token = "8703457324:AAF73WOjeXwtQ_yA7luPR6TNdF8VoD7Uwqs"

dp = Dispatcher()


async def set_commands_menu(bot):
    bot_commands = [
        BotCommand(command="/start", description="Запуск!"),
        BotCommand(command="/help", description="Получить справку по работе с ботом"),
        BotCommand(command="/donat", description="Поддержать автора"),
    ]
    await bot.set_my_commands(bot_commands)

async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)


async def main():
    bot = Bot(token=tg_bot_token)

    await set_commands_menu(bot)

    await dp.start_polling(bot)

@dp.message(F.text=="/donation")
async def command_start(message: Message) -> None:
    await message.answer("Поддержать автора можно здесь{f}")

@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет!")

@dp.message(F.text=="/Help")
async def command_start(message: Message) -> None:
    await message.answer("Поддержка не отвечает")


if __name__ == "__main__":
    asyncio.run(main())