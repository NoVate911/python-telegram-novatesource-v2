from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.misc.translations import translations, user_language as get_user_language


def main(msg: Message) -> InlineKeyboardBuilder:
    user_langauge: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    ikb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['user']['help']['enter'], callback_data='user_help_enter'),
        InlineKeyboardButton(text=translations[user_langauge]['keyboards']['inline']['user']['donate'], callback_data='user_donate'),
    )
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