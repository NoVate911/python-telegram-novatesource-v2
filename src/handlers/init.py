from aiogram import Router, Dispatcher

from src.handlers.user.init import init as user_init
from src.handlers.other import router as other_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        other_router,
    )

    user_init(dp=dp)
    for router in routers:
        dp.include_router(router)