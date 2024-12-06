import sqlite3 
import functools

def with_db_connection(func):
    conn = sqlite3.connect('users.db')
    @functools.wraps(func)
    def wrapper(
        *args,
        **kwargs
    ):
        print(args, kwargs)    
        value = func(conn, *args, *kwargs)
        conn.close()
        return value
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id='dd2f3449-53ba-4c47-ad98-8e5f11850b6c')
print(user)
