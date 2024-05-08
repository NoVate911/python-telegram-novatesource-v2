from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from src.misc.keyboards.inline import main as main_ikb, administrator as administrator_ikb
from src.misc.filters import IsAdministrator
from src.misc.states import Administrator_PanelStates
from src.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.callback_query(StateFilter(None), IsAdministrator(), F.data.startswith('administrator_enter'))
async def callback_administrator_panel_enter(callback: CallbackQuery, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    await state.set_state(state=Administrator_PanelStates.MAIN.state)
    await callback.message.edit_text(text=translations[user_language]['messages']['administrator']['enter'], reply_markup=administrator_ikb(msg=callback))

@router.callback_query(StateFilter(Administrator_PanelStates.MAIN.state), F.data.startswith('administrator_exit'))
async def callback_administrator_panel_exit(callback: CallbackQuery, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    await state.set_state(state=None)
    await callback.message.edit_text(text=str.format(translations[user_language]['messages']['user']['start']['comeback'], callback.from_user.username), reply_markup=main_ikb(msg=callback))