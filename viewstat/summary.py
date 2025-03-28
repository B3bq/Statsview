import mysql.connector

def top_leagues():
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connction.cursor()

    sql_query = "SELECT name FROM league ORDER BY count DESC LIMIT 5"
    mycursor.execute(sql_query)
    top_league_names = mycursor.fetchall()
    return top_league_names

def top_teams():
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connction.cursor()

    sql_query = "SELECT name, (homeCount + awayCount) AS total_count FROM `teams` ORDER BY total_count DESC LIMIT 5"
    mycursor.execute(sql_query)

    top_teams_table = mycursor.fetchall()
    return top_teams_table