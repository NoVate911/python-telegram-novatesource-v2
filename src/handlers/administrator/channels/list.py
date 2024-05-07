from aiogram import Router, F
from aiogram.types import CallbackQuery, ChatFullInfo
from aiogram.filters import StateFilter
from aiogram.exceptions import TelegramBadRequest

from src.database.requests.select.channels import channels_all as select_channels_all
from src.misc.keyboards.inline import administrator_channels as administrator_channels_ikb
from src.misc.states import Administrator_ChannelsStates
from src.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.callback_query(StateFilter(Administrator_ChannelsStates.MAIN.state), F.data.startswith('administrator_channels_list'))
async def callback_administrator_channels_list(callback: CallbackQuery) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    channels_all: list | None = select_channels_all()
    if channels_all:
        channel_all_dict: str = []
        for channel in channels_all:
            channel_chat: ChatFullInfo = await callback.bot.get_chat(chat_id=f'@{channel[0]}')
            channel_all_dict.append(f"[{'+' if bool(channel[1]) else '-'}] <a href='https://t.me/{channel[0]}'>{channel_chat.title}</a>\n")
        
        all_channels: str = "".join(channel_all_dict)
        try:
            await callback.message.edit_text(text=str.format(translations[user_language]['messages']['administrator']['channels']['list'], all_channels), reply_markup=administrator_channels_ikb(msg=callback))
        except TelegramBadRequest:
            await callback.answer(text=translations[user_language]['pronouns']['already_selected'], show_alert=True)