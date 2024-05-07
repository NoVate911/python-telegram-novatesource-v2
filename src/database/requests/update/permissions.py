import json

from src.database.main import execute as database_execute


def permissions_permission_by_tid(tid: int, permission: dict) -> bool:
    return database_execute(sql='UPDATE permissions SET permission = %s WHERE tid = %s LIMIT 1', args=(json.dumps(obj=permission), tid))