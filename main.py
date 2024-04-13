#если нужны боты пишите мне tg @benetter
#в каждом файле поменяйте токен и айди на свой
from aiogram import Bot, Dispatcher
import asyncio
import logging
from db import db_start
from handlers import handlers,sechandlers,thirdhandlers

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token='ВАШ ТОКЕН')
    dp = Dispatcher()

    await db_start()
    dp.include_routers(handlers.router, sechandlers.router,thirdhandlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())