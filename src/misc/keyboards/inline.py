from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.database.requests.select.permissions import permissions_permission_by_tid as select_permissions_permission_by_tid
from src.misc.translations import translations, user_language as get_user_language


def main(msg: Message) -> InlineKeyboardBuilder:
    user_langauge: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    user_permission: dict = select_permissions_permission_by_tid(tid=msg.from_user.id)
    ikb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['user']['help']['enter'], callback_data='user_help_enter'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['user']['donate'], callback_data='user_donate'),
    )
    if bool(user_permission['administrator']):
        ikb.add(InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['enter'], callback_data='administrator_enter'))
        
    ikb.adjust(1)
    return ikb.as_markup()

def _help(msg: Message) -> InlineKeyboardBuilder:
    user_langauge: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    ikb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['user']['help']['information_bot'], callback_data='user_help_information_bot'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['user']['help']['exit'], callback_data='user_help_exit'),
    )
    ikb.adjust(1)
    return ikb.as_markup()

def administrator(msg: Message) -> InlineKeyboardBuilder:
    user_langauge: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    ikb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['channels']['enter'], callback_data='administrator_channels_enter'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['exit'], callback_data='administrator_exit'),
    )
    ikb.adjust(1)
    return ikb.as_markup()

def administrator_channels(msg: Message) -> InlineKeyboardBuilder:
    user_langauge: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    ikb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['channels']['add'], callback_data='administrator_channels_add'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['channels']['remove'], callback_data='administrator_channels_remove'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['channels']['change_status'], callback_data='administrator_channels_change_status'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['channels']['list'], callback_data='administrator_channels_list'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['administrator']['channels']['exit'], callback_data='administrator_channels_exit'),
    )
    ikb.adjust(1)
    return ikb.as_markup()