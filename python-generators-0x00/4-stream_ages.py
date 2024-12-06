seed = __import__('seed')


def stream_user_ages():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        yield row.get('age')


def average_age():
    total = sum(stream_user_ages())
    count = 0
    for age in stream_user_ages():
        count += 1
    print(f'Average age of users: {total/count}')
