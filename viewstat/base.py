import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")#execute function execute a sql query

#show all tables
for x in mycursor:
    print(x)