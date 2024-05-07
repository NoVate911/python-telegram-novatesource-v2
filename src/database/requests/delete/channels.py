from src.database.main import execute as database_execute


def channels_by_username(username: str) -> bool:
    return database_execute(sql='DELETE FROM channels WHERE username = %s LIMIT 1', args=(username))