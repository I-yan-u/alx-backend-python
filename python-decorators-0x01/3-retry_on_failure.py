import time
import sqlite3 
import functools


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            value = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return value
    return wrapper


def retry_on_failure(retries=3, delay=2):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            success = False
            retry = retries
            while not success and retry > -1:
                try:
                    # print(f'Running {func.__name__}({args, kwargs})')
                    value = func(*args, **kwargs)
                    success = True
                    return value
                except Exception:
                    # print(f'Trying Query again...(Retries left:{retry})')
                    time.sleep(delay)
                    retry -= 1
                    continue
        return wrapper
    return decorator_retry


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users2")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)