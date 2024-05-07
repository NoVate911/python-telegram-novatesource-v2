from src.database.main import execute as database_execute


def users_by_tid(tid: int) -> bool:
    return database_execute(sql='INSERT INTO users (tid) VALUES (%s)', args=(tid))