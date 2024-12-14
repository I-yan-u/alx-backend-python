import sqlite3


class DatabaseConnection:
    """DatabaseConnection class to simulate a Database connection"""
    def __init__(self):
        """Constructor method"""
        self.__db = None

    def __enter__(self):
        """Connect method"""
        self.__db = sqlite3.connect('users.db')
        return self.__db

    def __exit__(self, exc_type, exc_value, traceback):
        """Close method"""
        if self.__db:
            self.__db.close()
            self.__db = None
        return True

    def execute(self, query):
        """Execute method"""
        cursor = self.__db.cursor()
        cursor.execute(query)
        return cursor


if __name__ == '__main__':
    with DatabaseConnection() as db:
        cursor = db.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)