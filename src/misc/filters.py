import logging

from aiogram.types import Message, Chat, ChatMember
from aiogram.filters import Filter

from src.database.requests.select.channels import channels_all as select_channels_all
from src.database.requests.select.permissions import permissions_permission_by_tid as select_permissions_permission_by_tid
from src.database.requests.select.users import users_by_tid as select_users_by_tid


class IsRegistered(Filter):
    async def __call__(self, msg: Message) -> bool:
        return select_users_by_tid(tid=msg.from_user.id)

class NotRegistered(Filter):
    async def __call__(self, msg: Message) -> bool:
        return not select_users_by_tid(tid=msg.from_user.id)

class IsSubscribedChannels(Filter):
    async def __call__(self, msg: Message) -> bool:
        channels_all: list = select_channels_all()
        if channels_all:
            channels_need_subscribed: int = 0
            user_channels_need_subscribed: int = 0
            for channel in channels_all:
                if bool(channel[1]):
                    channel_chat: Chat = await msg.bot.get_chat(chat_id=f"@{channel[0]}")
                    if channel_chat.type == 'channel':
                        try:
                            user_channel_status: ChatMember = await msg.bot.get_chat_member(chat_id=f"@{channel[0]}", user_id=msg.from_user.id)
                            channels_need_subscribed += 1
                            if user_channel_status.status != 'left':
                                user_channels_need_subscribed += 1
                        except:
                            logging.error(f"You need to add a bot to the channel 'https://t.me/{channel[0]}', as an Administrator.")
            return True if user_channels_need_subscribed >= channels_need_subscribed else False
        else:
            return True

class NotSubscribedChannels(Filter):
    async def __call__(self, msg: Message) -> bool:
        channels_all: list = select_channels_all()
        if channels_all:
            channels_need_subscribed: int = 0
            user_channels_need_subscribed: int = 0
            for channel in channels_all:
                if bool(channel[1]):
                    channel_chat: Chat = await msg.bot.get_chat(chat_id=f"@{channel[0]}")
                    if channel_chat.type == 'channel':
                        try:
                            user_channel_status: ChatMember = await msg.bot.get_chat_member(chat_id=f"@{channel[0]}", user_id=msg.from_user.id)
                            channels_need_subscribed += 1
                            if user_channel_status.status != 'left':
                                user_channels_need_subscribed += 1
                        except:
                            logging.error(f"You need to add a bot to the channel 'https://t.me/{channel[0]}', as an Administrator.")
            return True if user_channels_need_subscribed < channels_need_subscribed else False
        else:
            return False
        
class IsAdministrator(Filter):
    async def __call__(self, msg: Message) -> bool:
        user_permission: dict = select_permissions_permission_by_tid(tid=msg.from_user.id)
        return bool(user_permission['administrator'])