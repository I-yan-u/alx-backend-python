import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries
def log_queries(func):
    @functools.wraps(func)
    def log_queries_wrapper(*args, **kwargs):
        for arg in args:
            print(arg)
        for k, v in kwargs.items():
            print(f'{datetime.now().time()} - {k} = {v}')
        return func(*args, **kwargs)
    return log_queries_wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")