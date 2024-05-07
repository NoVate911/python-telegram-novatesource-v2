from aiogram import Router, Dispatcher

from src.handlers.user.start import router as start_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        start_router,
    )

    for router in routers:
        dp.include_router(router)