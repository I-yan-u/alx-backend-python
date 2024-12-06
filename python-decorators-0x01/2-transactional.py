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


def transactional(func):
    @functools.wraps(func)
    def transaction_wrapper(*args, **kwargs):
        try:
            conn = args[0]
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            print(result)
            conn.commit()
    return transaction_wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 


update_user_email(user_id='dd2f3449-53ba-4c47-ad98-8e5f11850b6c', new_email='Crawford_Cartwright@hotmail.com')