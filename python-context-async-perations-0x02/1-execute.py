import sqlite3


class ExecuteQuery:
    """ExecuteQuery class to simulate a Database context manager"""
    def __init__(self, query, param=25):
        """Constructor method"""
        self.__conx = None
        self.__query = query
        self.__param = param

    def __enter__(self):
        """Connect method"""
        self.__conx = sqlite3.connect('users.db')
        cursor = self.__conx.cursor()
        cursor.execute(self.__query, (self.__param,))
        result = cursor.fetchall()
        return result
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Close method"""
        if self.__conx:
            self.__conx.close()
            self.__conx = None
        return True
    

if __name__ == '__main__':
    with ExecuteQuery("SELECT * FROM users WHERE age < ?", param=23) as results:
        for row in results:
            print(row)
