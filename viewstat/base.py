import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    base = "stats"
)

mycursor = mydb.cursor()

sql_league_check = "SELECT * FROM league WHERE name = %s"
LeagueName = "pl"

mycursor.execute(sql_league_check, LeagueName)#execute function execute a sql query

myresult = mycursor.fetchall()

#show all tables
for x in myresult:
    print(x)