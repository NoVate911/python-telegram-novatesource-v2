import logging

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ChatFullInfo
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext

from src.database.requests.insert.channels import channels as insert_channels
from src.database.requests.select.channels import channels_by_username as select_channels_by_username
from src.misc.keyboards.inline import administrator_channels as administrator_channels_ikb
from src.misc.states import Administrator_ChannelsStates
from src.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.message(StateFilter(Administrator_ChannelsStates.ADD.state), Command(commands=['cancel']))
async def callback_administrator_channels_add_cancel(msg: Message, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    user_data: dict = await state.get_data()
    await state.clear()
    await state.set_state(state=Administrator_ChannelsStates.MAIN.state)
    await msg.delete()
    await msg.bot.edit_message_text(text=translations[user_language]['messages']['administrator']['channels']['cancel'], chat_id=msg.from_user.id, message_id=user_data['administrator_channels_add_message_id'], reply_markup=administrator_channels_ikb(msg=msg))

@router.callback_query(StateFilter(Administrator_ChannelsStates.MAIN.state), F.data.startswith('administrator_channels_add'))
async def callback_administrator_channels_add_insert_username(callback: CallbackQuery, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    await state.set_state(state=Administrator_ChannelsStates.ADD.state)
    message: Message = await callback.message.edit_text(text=translations[user_language]['messages']['administrator']['channels']['add']['username'], reply_markup=None)
    await state.update_data(administrator_channels_add_message_id=message.message_id)

@router.message(StateFilter(Administrator_ChannelsStates.ADD.state), F.text)
async def callback_administrator_channels_add_check(msg: Message, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    user_data: dict = await state.get_data()
    await msg.delete()
    await state.clear()
    await state.set_state(state=Administrator_ChannelsStates.MAIN.state)
    max_length: int = 32
    if len(msg.text) > max_length:
        await msg.bot.edit_message_text(text=translations[user_language]['messages']['administrator']['channels']['add']['not_found'], chat_id=msg.from_user.id, message_id=user_data['administrator_channels_add_message_id'], reply_markup=administrator_channels_ikb(msg=msg))
        return
    
    try:
        channel_chat: ChatFullInfo = await msg.bot.get_chat(chat_id=f'@{msg.text}')
        if channel_chat.type == 'channel':
            channel_bot_member = await msg.bot.get_chat_member(chat_id=f'@{msg.text}', user_id=msg.from_user.id)
            if channel_bot_member.status != 'left':
                if not select_channels_by_username(username=msg.text):
                    if insert_channels(username=msg.text):
                        await msg.bot.edit_message_text(text=str.format(translations[user_language]['messages']['administrator']['channels']['add']['success'], msg.text), chat_id=msg.from_user.id, message_id=user_data['administrator_channels_add_message_id'], reply_markup=administrator_channels_ikb(msg=msg))
                else:
                    await msg.bot.edit_message_text(text=translations[user_language]['messages']['administrator']['channels']['add']['already'], chat_id=msg.from_user.id, message_id=user_data['administrator_channels_add_message_id'], reply_markup=administrator_channels_ikb(msg=msg))
    except Exception as ex:
        await msg.bot.edit_message_text(text=translations[user_language]['messages']['administrator']['channels']['add']['not_found'], chat_id=msg.from_user.id, message_id=user_data['administrator_channels_add_message_id'], reply_markup=administrator_channels_ikb(msg=msg))
        logging.error(ex)