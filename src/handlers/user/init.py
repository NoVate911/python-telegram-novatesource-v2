from aiogram import Router, Dispatcher

from src.handlers.user.help.init import init as help_init
from src.handlers.user.start import router as start_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        start_router,
    )

    help_init(dp=dp)
    for router in routers:
        dp.include_router(router)