from src.database.main import query as database_query, query_single as database_query_single


def channels_all() -> list | None:
    return database_query("SELECT * FROM channels")