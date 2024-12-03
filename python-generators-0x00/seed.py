#!/usr/bin/python3
import mysql.connector
import sys


def connect_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user=sys.argv[1],
    password=sys.argv[2]
    )
    return mydb


def show_databases(connection):
    mycursor = connection.cursor()
    mycursor.execute("SHOW DATABASES")
    for db in mycursor: print(db)


def create_database(connection):
    try:
        mycursor = connection.cursor()
        mycursor.execute("CREATE DATABASE ALX_prodev")
    except Exception:
        pass


def connect_to_prodev():
    mydb = mysql.connector.connect(
    host="localhost",
    user=sys.argv[1],
    password=sys.argv[2],
    database='ALX_prodev'
    )
    return mydb


def create_table(connection):
    try:
        mycursor = connection.cursor()
        mycursor.execute("\
                     CREATE TABLE user_data\
                     (user_id VARCHAR(64) PRIMARY KEY,\
                     name VARCHAR(32) NOT NULL, email VARCHAR(32) NOT NULL,\
                     age DECIMAL NOT NULL)")
    except Exception:
        pass


def show_tables(connection):
    mycursor = connection.cursor()
    mycursor.execute("SHOW TABLES")
    for tb in mycursor: print(tb)


def insert_data(connection, data):
    try:
        mycursor = connection.cursor()
        sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %f)"
        lines = (line for line in open(data))
        clean_lines = (line.rstrip().split(',') for line in lines)
        _ = next(clean_lines)
        for u_data in clean_lines:
            mycursor.execute(sql, tuple(u_data))
        connection.commit()
    except Exception:
        pass


if __name__ == '__main__':
    connection = connect_db()
    create_database(connection)
    # show_databases(connection)
    connection.close()
    connection = connect_to_prodev()
    create_table(connection)
    show_tables(connection)