from connect import connect
from insert import User

# connection to database
connection = connect()
if connection is None:
    print("No connection")
else:
    mycursor = connection.cursor(buffered=True)

# selecting names and counts for league
def top_leagues(sport):
    match sport:
        case "League of legends":
            sport = "lol_leagues"
            sql_query = f"SELECT {sport}.name, count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY count DESC LIMIT 5"
        case "Counter Strike":
            sport = "cs_leagues"
            sql_query = f"SELECT {sport}.name, count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY count DESC LIMIT 5"
        case _:
            if User.season == 'season':
                sport = sport.lower() + "_leagues_season"
                sql_query = f"SELECT {sport}.name, count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY count DESC LIMIT 5"
            else:
                sport = sport.lower() + "_leagues_year"
                sql_query = f"SELECT {sport}.name, count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY count DESC LIMIT 5"

    mycursor.execute(sql_query)
    top_league_names = mycursor.fetchall()
    return top_league_names

# selecting names and total count for teams
def top_teams(sport):
    match sport:
        case "League of legends":
            sport = "lol_teams"
            sql_query = f"SELECT {sport}.name, (home_count + away_count) AS total_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY total_count DESC LIMIT 5"
        case "Counter Strike":
            sport = "cs_teams"
            sql_query = f"SELECT {sport}.name, (home_count + away_count) AS total_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY total_count DESC LIMIT 5"
        case _:
            if User.season == 'season':
                sport = sport + "_teams_season"
                sql_query = f"SELECT {sport}.name, (home_count + away_count) AS total_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY total_count DESC LIMIT 5"
            else:
                sport = sport + "_teams_year"
                sql_query = f"SELECT {sport}.name, (home_count + away_count) AS total_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY total_count DESC LIMIT 5"

    mycursor.execute(sql_query)
    top_teams_table = mycursor.fetchall()
    return top_teams_table

# selecting names and home count
def home_team(sport):
    match sport:
        case "League of legends":
            sport = "lol_teams"
            sql_home_team = f"SELECT {sport}.name, home_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY home_count DESC LIMIT 1"
        case "Counter Strike":
            sport = "cs_teams"
            sql_home_team = f"SELECT {sport}.name, home_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY home_count DESC LIMIT 1"
        case _:
            if User.season == 'season':
                sport = sport + "_teams_season"
                sql_home_team = f"SELECT {sport}.name, home_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY home_count DESC LIMIT 1"
            else:
                sport = sport + "_teams_year"
                sql_home_team = f"SELECT {sport}.name, home_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY home_count DESC LIMIT 1"

    mycursor.execute(sql_home_team)
    top_home_team = mycursor.fetchall()
    return top_home_team

# selecting names and away count
def away_team(sport):
    match sport:
        case "League of legends":
            sport = "lol_teams"
            sql_away_team = f"SELECT {sport}.name, away_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY away_count DESC LIMIT 1"
        case "Counter Strike":
            sport = "cs_teams"
            sql_away_team = f"SELECT {sport}.name, away_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY away_count DESC LIMIT 1"
        case _:
            if User.season == 'season':
                sport = sport + "_teams_season"
                sql_away_team = f"SELECT {sport}.name, away_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY away_count DESC LIMIT 1"
            else:
                sport = sport + "_teams_year"
                sql_away_team = f"SELECT {sport}.name, away_count, images.img FROM {sport} JOIN images ON {sport}.img = images.id WHERE id_user = {User.user_id} ORDER BY away_count DESC LIMIT 1"

    mycursor.execute(sql_away_team)
    top_away_team = mycursor.fetchall()
    return top_away_team