from src.database.main import query as database_query, query_single as database_query_single


def users_by_tid(tid: int) -> bool:
    result: list | None = database_query_single(sql='SELECT COUNT(1) FROM users WHERE tid = %s', args=(tid))
    return result[0]

def users_language_code_by_tid(tid: int) -> str:
    result: list | None = database_query_single(sql='SELECT language_code FROM users WHERE tid = %s', args=(tid))
    return result[0]