from datetime import datetime
from pytz import timezone

from src.database.main import execute as database_execute


def logs(action: str) -> bool:
    return database_execute(sql='INSERT INTO logs (datetime, action) VALUES (%s, %s)', args=(datetime.now(tz=timezone(zone='Europe/Moscow')).strftime('%Y-%m-%d %H:%M'), action))