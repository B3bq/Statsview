import mysql.connector
import bcrypt # to password encryption

class User:
    user_id = ''


def add_datas_to_base(sport_name, *, league_name, teamOne_name, teamTwo_name):
    connect = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "statsview"
    )

    mycursor = connect.cursor(buffered=True)

    # where push datas
    match sport_name:
        case "League of legends":
            tabel_league = "lol_leagues"
            tabel_broker = "lol_broker"
            tabel_teams = "lol_teams"
        case "Counter Strike":
            tabel_league = "cs_leagues"
            tabel_broker = "cs_broker"
            tabel_teams = "cs_teams"
        case _:
            tabel_league = sport_name.lower() + "_leagues"
            tabel_broker = sport_name.lower() + "_broker"
            tabel_teams = sport_name.lower() + "_teams"

    # checking if exist a league
    sql_league_check = f"SELECT * FROM {tabel_league} WHERE name = %s AND id_user = %s"
    mycursor.execute(sql_league_check, (league_name, User.user_id)) #execute function execute a sql query
    myresult_league = mycursor.fetchall() #getting a result to list

    if myresult_league != []:
        sql_update_league = f"UPDATE {tabel_league} SET count = count + 1 WHERE name = %s AND id_user = %s"
        mycursor.execute(sql_update_league, (league_name, User.user_id))
    else:
        sql_insert_league = f"INSERT INTO {tabel_league} (id, id_user, name, count, img) VALUES (NULL, %s, %s, 1, '')"
        mycursor.execute(sql_insert_league, (User.user_id, league_name))



    # checking if team one exist
    sql_team_one_check = f"SELECT * FROM {tabel_teams} WHERE name = %s AND id_user = %s"
    mycursor.execute(sql_team_one_check, (teamOne_name, User.user_id))
    myresult_team_one = mycursor.fetchall()

    if myresult_team_one != []:
        sql_update_teamone = f"UPDATE {tabel_teams} SET homeCount = homeCount + 1 WHERE name = %s AND id_user = %s"
        mycursor.execute(sql_update_teamone, (teamOne_name, User.user_id))
    else:
        sql_insert_teamone = f"INSERT INTO {tabel_teams} (id, id_user, name, homeCount, awayCount, img) VALUES (NULL, %s, %s, 1, 0, '')"
        mycursor.execute(sql_insert_teamone, (User.user_id, teamOne_name))



    # checking if team two exist
    sql_team_one_check = f"SELECT * FROM {tabel_teams} WHERE name = %s AND id_user = %s"
    mycursor.execute(sql_team_one_check, (teamTwo_name, User.user_id))
    myresult_team_one = mycursor.fetchall()

    if myresult_team_one != []:
        sql_update_teamone = f"UPDATE {tabel_teams} SET awayCount = awayCount + 1 WHERE name = %s AND id_user = %s"
        mycursor.execute(sql_update_teamone, (teamTwo_name, User.user_id))
    else:
        sql_insert_teamone = f"INSERT INTO {tabel_teams} (id, id_user, name, homeCount, awayCount, img) VALUES (NULL, %s, %s, 0, 1, '')"
        mycursor.execute(sql_insert_teamone, (User.user_id, teamTwo_name))



    # taking id from league table
    sql_take_idleague = f"SELECT id FROM {tabel_league} WHERE name = %s"
    mycursor.execute(sql_take_idleague, (league_name,))
    result = mycursor.fetchone() # take first record
    idLeague = result[0] # take id
    print(idLeague)

    # taking id for teams
    teams = [teamOne_name, teamTwo_name]
    idTeams = []
    print(teams)

    sql_take_idteam = f"SELECT id FROM {tabel_teams} WHERE name = %s"
    for item in teams:
        mycursor.execute(sql_take_idteam, (item,))
        result = mycursor.fetchone()

        idTeam = result[0]
        idTeams.append(idTeam)
    #sql_check_exist = f"SELECT id_teams FROM {tabel_broker} JOIN {tabel_teams} ON {tabel_broker}.id_teams = {tabel_teams}.id WHERE {tabel_broker}.id_league = %s AND {tabel_teams}.name = %s LIMIT 1"
    #for item in teams:
    #    mycursor.execute(sql_check_exist, (idLeague, item))
    #    exists = mycursor.fetchone()
    
    #    if exists:
    #        print(f"⚠ Team {item} is already exist")
    #        continue

    #    mycursor.execute(sql_take_idteam, (item,))
    #    result = mycursor.fetchone()
    #    
    #    if result:
    #        idTeam = result[0]
    #        idTeams.append(idTeam)

    print(idTeams)

    # insert teams to leagues_teams table
    sql_insert = f"INSERT IGNORE INTO {tabel_broker} VALUES (%s, %s)"
    for item in idTeams:
            mycursor.execute(sql_insert, (idLeague, item))

    print(f"Added teams {teams[0]} and {teams[1]} to the competition {league_name}")

    connect.commit()
    connect.close()
    
def insert_user(name, mail, password):
    connect = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "stat"
    )

    mycursor = connect.cursor()

    # changing varibles to list
    Name = [name]
    mail = mail
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # checking user
    sql_check = "SELECT * FROM users WHERE name = %s"
    mycursor.execute(sql_check, Name)
    myresult = mycursor.fetchall()

    if myresult != []:
        return False
    else:
        sql_insert = "INSERT INTO users (idusers, mail, name, pass) VALUES (NULL, %s, %s, %s)"
        mycursor.execute(sql_insert, (mail, name, hashed))

    connect.commit()
    connect.close()
    return True

def check_user(login, password):
    connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'stat'
    )

    mycursor = connect.cursor()

    sql_check = "SELECT mail, name FROM users WHERE mail = %s or name = %s"
    mycursor.execute(sql_check, (login, login))
    myresult = mycursor.fetchall()

    if myresult != []:
        sql_pass_check = "SELECT pass FROM users WHERE name = %s or mail = %s"
        mycursor.execute(sql_pass_check, (login, login))
        myresult = mycursor.fetchone()
        hash_pass = myresult[0].encode()
        
        if bcrypt.checkpw(password.encode(), hash_pass):
            sql_user_id = "SELECT idusers FROM users WHERE name = %s or mail = %s"
            mycursor.execute(sql_user_id, (login, login))
            result = mycursor.fetchone()
            user_id = result[0]
            print(user_id)

            connect.close()
            return user_id
        else:
            text = "Incorrect password"
            return text
    else:
        text = "User don't exist"
        return text