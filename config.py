TOKEN: str = 'YOUR_TOKEN'

OWNER_TELEGRAM_ID: int = []

DATABASE_SETTINGS: str = {
    'host': "localhost",
    'user': "root",
    'password': "",
    'database': "telegram-novatesource",
    'port': 3306,
}

# https://aaio.so/
SHOP_SETTINGS: str = {
    'merchant_id': "YOUR_SHOP_ID", # ID Вашего магазина
    'currency': "RUB", # Валюта заказа
    'secret': "YOUR_SECRET_KEY", # Секретный ключ №1 из настроек магазина
    'desc': "Пожертвование на развитие", # Описание заказа
    'lang': "ru", # Язык формы
}