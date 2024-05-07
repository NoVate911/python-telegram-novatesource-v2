from aiogram import Router, F
from aiogram.types import CallbackQuery, User
from aiogram.filters import StateFilter
from aiogram.exceptions import TelegramBadRequest

from src.misc.keyboards.inline import _help as help_ikb
from src.misc.states import User_HelpStates
from src.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.callback_query(StateFilter(User_HelpStates.MAIN.state), F.data.startswith('user_help_information_bot'))
async def callback_user_help_bot(callback: CallbackQuery) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    try:
        bot: User = await callback.bot.get_me()
        await callback.message.edit_text(text=str.format(translations[user_language]['messages']['user']['help']['information_bot'], bot.username), reply_markup=help_ikb(msg=callback))
    except TelegramBadRequest:
        await callback.answer(text=translations[user_language]['pronouns']['already_selected'], show_alert=True)