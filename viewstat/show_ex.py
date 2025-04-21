import mysql.connector

# function to show league names
def show_leagues(sport):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test"
    )

    mycursor = connection.cursor()

    match sport:
        case "League of legends":
            sport = "lol_leagues"
        case "Counter Strike":
            sport = "cs_leagues"
        case _:
            sport = sport + "_leagues"

    # league options
    sql_league = f"SELECT name FROM {sport}"
    mycursor.execute(sql_league)
    league_names = mycursor.fetchall()

    league_names = [name[0] for name in league_names] # loop which make a list

    connection.commit()
    connection.close()

    return league_names

# function to show team names
def show_teams(league_name, sport):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test"
    )

    mycursor = connection.cursor()

    # match correct tables
    match sport:
        case "League of legends":
            tabel_league = "lol_leagues"
            tabel_broker = "lol_broker"
            tabel_teams = "lol_teams"
        case "Counter Strike":
            tabel_league = "cs_leagues"
            tabel_broker = "cs_broker"
            tabel_teams = "cs_teams"
        case _:
            tabel_league = sport + "_leagues"
            tabel_broker = sport + "_broker"
            tabel_teams = sport + "_teams"

    sql_find_teams = f"SELECT {tabel_teams}.name FROM {tabel_teams} JOIN {tabel_broker} ON {tabel_teams}.id = {tabel_broker}.id_teams JOIN {tabel_league} ON {tabel_broker}.id_league = {tabel_league}.id WHERE {tabel_league}.name = %s"
    mycursor.execute(sql_find_teams, league_name)
    team_names = mycursor.fetchall()

    team_names = [name[0] for name in team_names] # loop which make a list

    return team_names