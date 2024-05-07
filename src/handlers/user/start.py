from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import StateFilter, CommandStart

from config import OWNER_TELEGRAM_ID
from src.database.requests.insert.logs import logs as insert_logs
from src.database.requests.insert.permissions import permissions_by_tid as insert_permissions_by_tid
from src.database.requests.insert.users import users_by_tid as insert_users_by_tid
from src.database.requests.select.permissions import permissions_by_tid as select_permissions_by_tid, permissions_permission_by_tid as select_permissions_permission_by_tid
from src.database.requests.select.users import users_by_tid as select_users_by_tid
from src.database.requests.update.permissions import permissions_permission_by_tid as update_permissions_permission_by_tid
from src.misc.keyboards.inline import main as main_ikb
from src.misc.filters import IsSubscribedChannels
from src.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.message(StateFilter(None), IsSubscribedChannels(), CommandStart())
async def cmd_start(msg: Message) -> None:
    user_language: str = get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    if not select_permissions_by_tid(tid=msg.from_user.id):
        insert_permissions_by_tid(tid=msg.from_user.id)

    for owner in OWNER_TELEGRAM_ID:
        if msg.from_user.id == owner:
            user_permission: dict = select_permissions_permission_by_tid(tid=msg.from_user.id)
            if not bool(user_permission['administrator']):
                user_permission['administrator'] = int(not bool(user_permission['administrator']))
            update_permissions_permission_by_tid(tid=msg.from_user.id, permission=user_permission)

    if select_users_by_tid(tid=msg.from_user.id):
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['start']['comeback'], msg.from_user.username), reply_markup=main_ikb(msg=msg))
    else:
        if insert_users_by_tid(tid=msg.from_user.id):
            insert_logs(action=f"{msg.from_user.id} зарегистрировался в боте")
            await msg.reply(text=str.format(translations[user_language]['messages']['user']['start']['welcome'], msg.from_user.username), reply_markup=main_ikb(msg=msg))
        else:
            await msg.reply(text=translations[user_language]['messages']['user']['start']['error'], reply_markup=ReplyKeyboardRemove())