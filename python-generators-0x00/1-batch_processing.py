#!/usr/bin/python3
seed = __import__('seed')


def stream_users_in_batches(batch_size):
    cnx = seed.connect_to_prodev()
    if cnx:
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size}")
        data = cursor.fetchall()
        for row in data:
            yield row


def batch_processing(batch_size):
    for rows in stream_users_in_batches(batch_size):
        return rows if rows[-1] > 25 else ...
