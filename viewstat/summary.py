import mysql.connector

# selecting names and ciunts for league
def top_leagues():
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connction.cursor()

    sql_query = "SELECT name, count, img FROM league ORDER BY count DESC LIMIT 5"
    mycursor.execute(sql_query)
    top_league_names = mycursor.fetchall()
    connction.close()
    return top_league_names

# selecting names and total count for teams
def top_teams():
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connction.cursor()

    sql_query = "SELECT name, (homeCount + awayCount) AS total_count, img FROM `teams` ORDER BY total_count DESC LIMIT 5"
    mycursor.execute(sql_query)

    top_teams_table = mycursor.fetchall()
    connction.close()
    return top_teams_table

# selecting names and home count
def home_team():
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connction.cursor()

    sql_home_team = "SELECT name, homeCount, img FROM teams ORDER BY homeCount DESC LIMIT 1"
    mycursor.execute(sql_home_team)

    top_home_team = mycursor.fetchall()
    connction.close()
    return top_home_team

# selecting names and away count
def away_team():
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connction.cursor()

    sql_away_team = "SELECT name, awayCount, img FROM teams ORDER BY awayCount DESC LIMIT 1"
    mycursor.execute(sql_away_team)

    top_away_team = mycursor.fetchall()
    connction.close()
    return top_away_team