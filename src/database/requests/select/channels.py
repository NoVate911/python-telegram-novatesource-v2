from src.database.main import query as database_query, query_single as database_query_single


def channels_all() -> list | None:
    return database_query("SELECT * FROM channels")

def channels_by_username(username: str) -> bool:
    result: list | None = database_query_single(sql='SELECT COUNT(1) FROM channels WHERE username = %s', args=(username))
    return result[0]

def channels_status_by_username(username: str) -> int:
    result: list | None = database_query_single(sql='SELECT status FROM channels WHERE username = %s', args=(username))
    return result[0]