import mysql.connector

# function to show league names
def show_leagues():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connection.cursor()

    # league options
    sql_league = "SELECT name FROM league"
    mycursor.execute(sql_league)
    league_names = mycursor.fetchall()

    league_names = [name[0] for name in league_names] # loop which make a list

    connection.commit()
    connection.close()

    return league_names

# function to show team names
def show_teams(league_name):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stats"
    )

    mycursor = connection.cursor()

    sql_find_teams = "SELECT teams.name FROM teams JOIN leagues_teams ON teams.id = leagues_teams.teams_id JOIN league ON leagues_teams.leagues_id = league.id WHERE league.name = %s"
    mycursor.execute(sql_find_teams, league_name)
    team_names = mycursor.fetchall()

    team_names = [name[0] for name in team_names] # loop which make a list

    return team_names