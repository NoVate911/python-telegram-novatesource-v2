import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode

from config import TOKEN


async def start() -> None:
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    bot: Bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.info(msg="Bot stopped.")