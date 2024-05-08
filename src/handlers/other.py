import logging

from aiogram import Router
from aiogram.types import Message, Chat, ChatMember, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.database.requests.select.channels import channels_all as select_channels_all
from src.misc.keyboards.inline import main as main_ikb, _help as help_ikb, administrator as administrator_ikb, administrator_channels as administrator_channels_ikb
from src.misc.filters import NotRegistered, NotSubscribedChannels
from src.misc.states import User_HelpStates, User_DonateStates, Administrator_PanelStates, Administrator_ChannelsStates
from src.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.message(StateFilter('*'), NotSubscribedChannels())
async def need_subscribed(msg: Message, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    channels_all: list = select_channels_all()
    channel_need_subscribed: dict[str] = []
    for channel in channels_all:
        if bool(channel[1]):
            channel_chat: Chat = await msg.bot.get_chat(chat_id=f"@{channel[0]}")
            try:
                user_channel_status: ChatMember = await msg.bot.get_chat_member(chat_id=f"@{channel[0]}", user_id=msg.from_user.id)
                if user_channel_status.status == 'left':
                    channel_need_subscribed.append(f"<a href='https://t.me/{channel[0]}'>{channel_chat.title}</a>")
            except Exception as ex:
                logging.error(ex)
    channels_need_subscribed: dict[str] = "\n".join(channel_need_subscribed)
    await state.clear()
    await msg.reply(text=str.format(translations[user_language]['messages']['channels_need_subscribed'], channels_need_subscribed), reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter('*'), NotRegistered())
async def not_registered(msg: Message, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    await state.clear()
    await msg.reply(text=translations[user_language]['messages']['not_registered'], reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter(None, User_HelpStates.MAIN.state, User_DonateStates.CONFIRMATION.state, Administrator_PanelStates.MAIN.state, Administrator_ChannelsStates.MAIN.state))
async def cmd_unknown(msg: Message, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    current_state: str = await state.get_state()
    keyboard: ReplyKeyboardMarkup = main_ikb(msg=msg)
    if current_state:
        match(str(current_state.split(":")[0])):
            case 'User_HelpStates':
                keyboard = help_ikb(msg=msg)
            case 'Administrator_PanelStates':
                keyboard = administrator_ikb(msg=msg)
            case 'Administrator_ChannelsStates':
                keyboard = administrator_channels_ikb(msg=msg)

    await msg.reply(text=translations[user_language]['messages']['unknown'], reply_markup=keyboard)