import mysql.connector
from insert import User

# selecting names and ciunts for league
def top_leagues(sport):
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test"
    )

    mycursor = connction.cursor()

    match sport:
        case "League of legends":
            sport = "lol_leagues"
        case "Counter Strike":
            sport = "cs_leagues"
        case _:
            sport = sport.lower() + "_leagues"

    sql_query = f"SELECT name, count, img FROM {sport} WHERE id_user = {User.user_id} ORDER BY count DESC LIMIT 5"
    mycursor.execute(sql_query)
    top_league_names = mycursor.fetchall()
    connction.close()
    return top_league_names

# selecting names and total count for teams
def top_teams(sport):
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test"
    )

    mycursor = connction.cursor()

    match sport:
        case "League of legends":
            sport = "lol_teams"
        case "Counter Strike":
            sport = "cs_teams"
        case _:
            sport = sport + "_teams"

    sql_query = f"SELECT name, (homeCount + awayCount) AS total_count, img FROM {sport} WHERE id_user = {User.user_id} ORDER BY total_count DESC LIMIT 5"
    mycursor.execute(sql_query)

    top_teams_table = mycursor.fetchall()
    connction.close()
    return top_teams_table

# selecting names and home count
def home_team(sport):
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test"
    )

    mycursor = connction.cursor()

    match sport:
        case "League of legends":
            sport = "lol_teams"
        case "Counter Strike":
            sport = "cs_teams"
        case _:
            sport = sport + "_teams"

    sql_home_team = f"SELECT name, homeCount, img FROM {sport} WHERE id_user = {User.user_id} ORDER BY homeCount DESC LIMIT 1"
    mycursor.execute(sql_home_team)

    top_home_team = mycursor.fetchall()
    connction.close()
    return top_home_team

# selecting names and away count
def away_team(sport):
    # connection to database
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test"
    )

    mycursor = connction.cursor()

    match sport:
        case "League of legends":
            sport = "lol_teams"
        case "Counter Strike":
            sport = "cs_teams"
        case _:
            sport = sport + "_teams"

    sql_away_team = f"SELECT name, awayCount, img FROM {sport} WHERE id_user = {User.user_id} ORDER BY awayCount DESC LIMIT 1"
    mycursor.execute(sql_away_team)

    top_away_team = mycursor.fetchall()
    connction.close()
    return top_away_team