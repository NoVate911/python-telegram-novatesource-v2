from src.database.main import execute as database_execute


def permissions_by_tid(tid: int) -> bool:
    return database_execute(sql='INSERT INTO permissions (tid) VALUES (%s)', args=(tid))