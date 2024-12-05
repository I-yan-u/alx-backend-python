from itertools import islice


seed = __import__('seed')

def stream_users():
    cnx = seed.connect_to_prodev()
    if cnx:
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM user_data")
        data = cursor.fetchall()
        for row in data:
            yield row

if __name__ == '__main__':
    for user in islice(stream_users(), 6):
        print(user)