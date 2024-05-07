import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode

from config import TOKEN
from src.database.main import init as database_init, close as database_close
from src.handlers.init import init as handlers_init


async def start() -> None:
    if not database_init():
        return

    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    bot: Bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)

    handlers_init(dp=dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        database_close()
        logging.info(msg="Bot stopped.")