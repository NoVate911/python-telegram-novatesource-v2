from typing import Final

from aiogram.fsm.state import State, StatesGroup


# USER
class HelpStates(StatesGroup):
    MAIN: Final = State()