import mysql.connector
from mysql.connector import Error


def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="statsview"
        )
        return connection
    except Error as e:
        print("Database connection failed:", e)
        return None