from typing import Final

from aiogram.fsm.state import State, StatesGroup


# USER
class User_HelpStates(StatesGroup):
    MAIN: Final = State()

# ADMINISTRATOR
class Administrator_PanelStates(StatesGroup):
    MAIN: Final = State()

class Administrator_ChannelsStates(StatesGroup):
    MAIN: Final = State()

    ADD: Final = State()
    REMOVE: Final = State()
    CHANGE_STATUS: Final = State()