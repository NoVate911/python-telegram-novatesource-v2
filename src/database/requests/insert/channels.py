from src.database.main import execute as database_execute


def channels(username: str) -> bool:
    return database_execute(sql='INSERT INTO channels (username) VALUES (%s)', args=(username))