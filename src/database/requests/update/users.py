from src.database.main import execute as database_execute


def users_language_code_by_tid(tid: int, language_code: str) -> bool:
    return database_execute(sql='UPDATE users SET language_code = %s WHERE tid = %s LIMIT 1', args=(language_code, tid))