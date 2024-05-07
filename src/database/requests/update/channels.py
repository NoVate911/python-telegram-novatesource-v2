from src.database.main import execute as database_execute


def channels_status_by_username(username: str, status: int) -> bool:
    return database_execute(sql='UPDATE channels SET status = %s WHERE username = %s LIMIT 1', args=(status, username))