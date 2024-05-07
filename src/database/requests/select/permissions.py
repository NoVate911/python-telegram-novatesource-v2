import json

from src.database.main import query as database_query, query_single as database_query_single


def permissions_by_tid(tid: int) -> bool:
    result: list | None = database_query_single(sql='SELECT COUNT(1) FROM permissions WHERE tid = %s', args=(tid))
    return result[0]

def permissions_permission_by_tid(tid: int) -> dict:
    return json.loads(s=database_query_single(sql='SELECT permission FROM permissions WHERE tid = %s LIMIT 1', args=(tid))[0])