import asyncio
from aiogram import Bot, Dispatcher
from handlers import menu, form_handlers

TOKEN = "Add_Your_Telegram_Bot_Token_Here"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(menu.router)
    dp.include_router(form_handlers.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
