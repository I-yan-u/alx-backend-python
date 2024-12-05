#!/usr/bin/python3
import mysql.connector
from dotenv import load_dotenv
import os
from uuid import uuid4


load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASS')


def connect_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password
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
    user=user,
    password=password,
    database='ALX_prodev'
    )
    return mydb


def create_table(connection):
    try:
        mycursor = connection.cursor()
        mycursor.execute("\
                     CREATE TABLE user_data\
                     (user_id VARCHAR(64) PRIMARY KEY,\
                     name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL,\
                     age DECIMAL NOT NULL)")
    except Exception:
        pass


def show_tables(connection):
    mycursor = connection.cursor()
    mycursor.execute("SHOW TABLES")
    for tb in mycursor: print(tb)


def insert_data(connection, data):
    # try:
    mycursor = connection.cursor()
    sql = """INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"""
    lines = (line for line in open(data))
    clean_lines = (line.rstrip().split(',') for line in lines)
    _ = next(clean_lines)
    vals: list[tuple] = []
    for u_data in clean_lines:
        age = float(u_data.pop().strip('"'))
        val = [str(uuid4()), *u_data, age]
        vals.append(tuple(val))
    mycursor.executemany(sql, vals)
    connection.commit()
    print(mycursor.rowcount, "was inserted.")
    # except Exception:
    #     pass


if __name__ == '__main__':
    connection = connect_db()
    create_database(connection)
    connection.close()
    connection = connect_to_prodev()
    create_table(connection)
    show_tables(connection)
