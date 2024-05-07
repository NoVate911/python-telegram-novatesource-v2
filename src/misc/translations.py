from src.database.requests.select.users import users_by_tid as select_users_by_tid, users_language_code_by_tid as select_users_language_code_by_tid
from src.database.requests.update.users import users_language_code_by_tid as update_users_language_code_by_tid


languages: str = ['ru']
translations: str = {
    'ru': {
        'pronouns': {
            'already_selected': "Вы уже выбрали данный раздел.",
        },
        'messages': {
            'channels_need_subscribed': "📌 <b>Для того, чтобы пользоваться ботом нужно подписаться на следующие каналы:</b>\n\n"\
                "{0}",
            'not_registered': "📌 Для того, чтобы пользоваться ботом нужно пройти регистрацию через команду - /start.",
            'unknown': "⚠️ <b>Команда не найдена или не определена!</b>\n"\
                "👇 Используй кнопки ниже для навигации.",
            'user': {
                'start': {
                    'welcome': "👋 Добро пожаловать, @{0}.\n\n"\
                        "🗣 Я создан для того, чтобы помогать участникам канала <a href='https://t.me/novatesource'>NoVate Source</a> в поиске необходимой информации.\n"\
                        "👇 Для навигации по моим функциям используйте кнопки, которые показаны ниже.\n\n"\
                        "🤝 Приятного пользования и продуктивного дня!",
                    'comeback': "🔥 Я определил ваш аккаунт, @{0}.\n"\
                        "👇 Используйте кнопки ниже для навигации.",
                    'error': "⚠️ <b>При регистрации/авторизации произошла ошибка!</b>\n"\
                        "📌 Скоро всё будет исправлено.",
                },
                'help': {
                    'enter': "☺️ Я с радостью подскажу то, что требуется.\n"\
                        "👇 Выберите нужный пункт ниже.",
                    'information_bot': "🤖 @{0} - бот-помощник, который создан специально для канала @novatesource.",
                },
            },
            'administrator': {
                'enter': "📌 Вы в панели Администратора.\n"\
                    "ℹ️ Контролируйте множество систем не останавливая бота.",
                'channels': {
                    'enter': "📌 Управляйте каналами для подписки прямо в боте, без его остановки.",
                    'cancel': "✅ Вы отменили действие.",
                    'add': {
                        'username': "⌨️ Введите название канала <span class='tg-spoiler'>(без @)</span>:\n\n"\
                            "📌 Для отмены - /cancel",
                        'not_found': "❌ Канал с таким названием не найден или бот не добавлен, как Администратор.",
                        'already': "⚠️ Канал с таким названием уже добавлен.",
                        'success': "✅ Канал @{0} добавлен.\n"\
                            "📌 Для смены типа подписки используйте клавиатуру.",
                    },
                    'remove': {
                        'username': "⌨️ Введите название канала <span class='tg-spoiler'>(без @)</span>:\n\n"\
                            "📌 Для отмены - /cancel",
                        'not_found': "❌ Канал с таким названием не добавлен в бота.",
                        'success': "✅ Канал @{0} удален.",
                    },
                    'change_status': {
                        'username': "⌨️ Введите название канала <span class='tg-spoiler'>(без @)</span>:\n\n"\
                            "📌 Для отмены - /cancel",
                        'not_found': "❌ Канал с таким названием не добавлен в бота.",
                        'success': "✅ Тип подписки для канала @{0} изменен на <b>{1}</b>.",
                    },
                    'list': "📄 Список добавленных каналов:\n"\
                        "{0}",
                },
            },
        },
        'keyboards': {
            'inline': {
                'user': {
                    'help': {
                        'enter': "🧷 ПОМОЩЬ",
                        'information_bot': "⚙️ ИНФОРМАЦИЯ О БОТЕ",
                        'exit': "⬅️ НАЗАД",
                    },
                    'donate': "💰 ПОЖЕРТВОВАТЬ",
                },
                'administrator': {
                    'enter': "🎈 АДМИНИСТРАТОР",
                    'channels': {
                        'enter': "📢 УПРАВЛЕНИЕ КАНАЛАМИ",
                        'add': "📥 ДОБАВИТЬ",
                        'remove': "📤 УДАЛИТЬ",
                        'change_status': "⚙️ СМЕНИТЬ ТИП",
                        'list': "📄 СПИСОК",
                        'exit': "⬅️ НАЗАД",
                    },
                    'exit': "⬅️ НАЗАД",
                },
            },
        },
    },
}


def user_language(telegram_id: int, language_code: str) -> str:
    if not language_code in languages:
        language_code = 'ru'
    if select_users_by_tid(tid=telegram_id):
        if select_users_language_code_by_tid(tid=telegram_id) != language_code:
            update_users_language_code_by_tid(tid=telegram_id, language_code=language_code)
    return language_code