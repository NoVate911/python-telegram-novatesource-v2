from hashlib import sha256
from urllib.parse import urlencode
from datetime import datetime
from pytz import timezone

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext

from src.misc.keyboards.inline import main as main_ikb, donate_confirmation as donate_confirmation_ikb
from src.misc.states import User_DonateStates
from src.misc.translations import translations, user_language as get_user_language

from config import SHOP_SETTINGS


router: Router = Router()


@router.message(StateFilter(User_DonateStates.AMOUNT_INSERT.state), Command(commands=['cancel']))
async def callback_user_donate_cancel(msg: Message, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    user_data: dict = await state.get_data()
    await state.clear()
    await msg.delete()
    await msg.bot.edit_message_text(text=translations[user_language]['messages']['user']['donate']['cancel'], chat_id=msg.from_user.id, message_id=user_data['user_donate_amount_message_id'], reply_markup=main_ikb(msg=msg))

@router.callback_query(StateFilter(None), F.data.startswith('user_donate'))
async def callback_user_donate_amount_insert(callback: CallbackQuery, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    await state.set_state(state=User_DonateStates.AMOUNT_INSERT.state)
    message: Message = await callback.message.edit_text(text=translations[user_language]['messages']['user']['donate']['amount']['insert'], reply_markup=None)
    await state.update_data(user_donate_amount_message_id=message.message_id)

@router.message(StateFilter(User_DonateStates.AMOUNT_INSERT.state), F.text)
async def callback_user_donate_amount_check(msg: Message, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    user_data: dict = await state.get_data()
    await msg.delete()
    await state.clear()
    if not msg.text.isdigit():
        await msg.bot.edit_message_text(text=translations[user_language]['messages']['user']['donate']['amount']['incorrect_format'], chat_id=msg.from_user.id, message_id=user_data['user_donate_amount_message_id'], reply_markup=main_ikb(msg=msg))
        return
    
    await state.set_state(state=User_DonateStates.CONFIRMATION.state)
    donate_sign: str = f':'.join([
        SHOP_SETTINGS['merchant_id'],
        msg.text,
        SHOP_SETTINGS['currency'],
        SHOP_SETTINGS['secret'],
        f'{msg.from_user.id}_{datetime.now(tz=timezone(zone='Europe/Moscow')).strftime(format='%Y/%m/%d %H-%M')}',
    ])
    donate_params: str = {
        'merchant_id': SHOP_SETTINGS['merchant_id'],
        'amount': msg.text,
        'currency': SHOP_SETTINGS['currency'],
        'order_id': f'{msg.from_user.id}_{datetime.now(tz=timezone(zone='Europe/Moscow')).strftime(format='%Y/%m/%d %H-%M')}',
        'sign': sha256(donate_sign.encode('utf-8')).hexdigest(),
        'desc': SHOP_SETTINGS['desc'],
        'lang': SHOP_SETTINGS['lang'],
    }
    await msg.bot.edit_message_text(text=str.format(translations[user_language]['messages']['user']['donate']['success'], msg.text), chat_id=msg.from_user.id, message_id=user_data['user_donate_amount_message_id'], reply_markup=donate_confirmation_ikb(msg=msg, redirect_link=f'https://aaio.so/merchant/pay?{urlencode(donate_params)}'))

@router.callback_query(StateFilter(User_DonateStates.CONFIRMATION.state), F.data.startswith('user_donate_confirmation_exit'))
async def callback_user_donate_confirmation_exit(callback: CallbackQuery, state: FSMContext) -> None:
    user_language: str = get_user_language(telegram_id=callback.from_user.id, language_code=callback.from_user.language_code)
    await state.clear()
    await callback.message.edit_text(text=str.format(translations[user_language]['messages']['user']['start']['comeback'], callback.from_user.username), reply_markup=main_ikb(msg=callback))