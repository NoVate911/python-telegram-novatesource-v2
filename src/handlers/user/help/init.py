from aiogram import Router, Dispatcher

from src.handlers.user.help.main import router as main_router
from src.handlers.user.help.bot import router as bot_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        main_router,
        bot_router,
    )

    for router in routers:
        dp.include_router(router)