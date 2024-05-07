from aiogram import Router, Dispatcher

from src.handlers.administrator.channels.main import router as main_router
from src.handlers.administrator.channels.add import router as add_router
from src.handlers.administrator.channels.remove import router as remove_router
from src.handlers.administrator.channels.change_status import router as change_status_router
from src.handlers.administrator.channels.list import router as list_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        main_router,
        add_router,
        remove_router,
        change_status_router,
        list_router,
    )

    for router in routers:
        dp.include_router(router)