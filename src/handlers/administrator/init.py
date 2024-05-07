from aiogram import Router, Dispatcher

from src.handlers.administrator.channels.init import init as channels_init
from src.handlers.administrator.main import router as main_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        main_router,
    )

    channels_init(dp=dp)
    for router in routers:
        dp.include_router(router)