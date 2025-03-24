import mysql.connector

# this file will be insert values to database

connetion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "stats"
)