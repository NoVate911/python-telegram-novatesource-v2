from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from src.misc.keyboards.inline import administrator as administrator_ikb, administrator_channels as administrator_channels_ikb
from src.misc.states import Administrator_PanelStates, Administrator_ChannelsStates
from src.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.callback_query(StateFilter(Administrator_PanelStates.MAIN.state), F.data.startswith('administrator_channels_enter'))
async def callback_administrator_channels_enter(callback: CallbackQuery, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    await state.set_state(state=Administrator_ChannelsStates.MAIN.state)
    await callback.message.edit_text(text=translations[user_language]['messages']['administrator']['channels']['enter'], reply_markup=administrator_channels_ikb(msg=callback))

@router.callback_query(StateFilter(Administrator_ChannelsStates.MAIN.state), F.data.startswith('administrator_channels_exit'))
async def callback_administrator_channels_exit(callback: CallbackQuery, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    await state.set_state(state=Administrator_PanelStates.MAIN.state)
    await callback.message.edit_text(text=translations[user_language]['messages']['administrator']['enter'], reply_markup=administrator_ikb(msg=callback))