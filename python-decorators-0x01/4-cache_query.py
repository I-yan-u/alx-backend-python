import time
import sqlite3 
import functools


query_cache = {}


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


def cache_query(func):
    @functools.wraps(func)
    def cache_wrapper(*args, **kwargs):
        params = [args, kwargs]
        key = f'{func.__name__}{params}'
        if key in query_cache:
            print(f'Getting result from cache...')
            return query_cache[key]
        print(f'Getting result from DB...')
        val = func(*args, **kwargs)
        query_cache[key] = val
        return val
    return cache_wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users LIMIT 10")
print(users)

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users LIMIT 10")
print(users_again)