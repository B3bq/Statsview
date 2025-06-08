import mysql.connector
import bcrypt # to password encryption

class User:
    user_id = ''
    season = ''


def add_datas_to_base(sport_name, *, league_name, teamOne_name, teamTwo_name):
    connect = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "database"
    )

    mycursor = connect.cursor(buffered=True)

    # where push datas
    match sport_name:
        case "League of legends":
            tabel_league = "lol_leagues"
            tabel_broker = "lol_broker"
            tabel_teams = "lol_teams"

            # checking if exist a league
            sql_league_check = f"SELECT * FROM {tabel_league} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_league_check, (league_name, User.user_id)) #execute function execute a sql query
            myresult_league = mycursor.fetchall() #getting a result to list

            if myresult_league != []:
                sql_update_league = f"UPDATE {tabel_league} SET count = count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_league, (league_name, User.user_id))       
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of league image
                mycursor.execute(sql_img_search, (league_name,))
                img = mycursor.fetchall()

                # if don't exist league name then img equal one (basic image for league)
                if img == []:
                    img = 1
                else:
                    img = img[0]

                sql_insert_league = f"INSERT INTO {tabel_league} (id, id_user, name, count, img) VALUES (NULL, %s, %s, 1, %s)"
                mycursor.execute(sql_insert_league, (User.user_id, league_name, img))

            # checking if team one exist
            sql_team_one_check = f"SELECT * FROM {tabel_teams} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_one_check, (teamOne_name, User.user_id))
            myresult_team_one = mycursor.fetchall()

            if myresult_team_one != []:
                sql_update_teamone = f"UPDATE {tabel_teams} SET home_count = home_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamOne_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamOne_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal two (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 1, 0, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamOne_name, img))

            # checking if team two exist
            sql_team_two_check = f"SELECT * FROM {tabel_teams} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_two_check, (teamTwo_name, User.user_id))
            myresult_team_two = mycursor.fetchall()

            if myresult_team_two != []:
                sql_update_teamone = f"UPDATE {tabel_teams} SET away_count = away_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamTwo_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamTwo_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal one (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 0, 1, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamTwo_name, img))
            
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
    
            # insert teams to broker table in year
            sql_insert = f"INSERT IGNORE INTO {tabel_broker} VALUES (%s, %s)"
            for item in idTeams:
                mycursor.execute(sql_insert, (idLeague, item))
        case "Counter Strike":
            tabel_league = "cs_leagues"
            tabel_broker = "cs_broker"
            tabel_teams = "cs_teams"
            # checking if exist a league
            sql_league_check = f"SELECT * FROM {tabel_league} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_league_check, (league_name, User.user_id)) #execute function execute a sql query
            myresult_league = mycursor.fetchall() #getting a result to list

            if myresult_league != []:
                sql_update_league = f"UPDATE {tabel_league} SET count = count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_league, (league_name, User.user_id))       
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of league image
                mycursor.execute(sql_img_search, (league_name,))
                img = mycursor.fetchall()

                # if don't exist league name then img equal one (basic image for league)
                if img == []:
                    img = 1
                else:
                    img = img[0]

                sql_insert_league = f"INSERT INTO {tabel_league} (id, id_user, name, count, img) VALUES (NULL, %s, %s, 1, %s)"
                mycursor.execute(sql_insert_league, (User.user_id, league_name, img))

            # checking if team one exist
            sql_team_one_check = f"SELECT * FROM {tabel_teams} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_one_check, (teamOne_name, User.user_id))
            myresult_team_one = mycursor.fetchall()

            if myresult_team_one != []:
                sql_update_teamone = f"UPDATE {tabel_teams} SET home_count = home_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamOne_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamOne_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal two (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 1, 0, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamOne_name, img))

            # checking if team two exist
            sql_team_two_check = f"SELECT * FROM {tabel_teams} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_two_check, (teamTwo_name, User.user_id))
            myresult_team_two = mycursor.fetchall()

            if myresult_team_two != []:
                sql_update_teamone = f"UPDATE {tabel_teams} SET away_count = away_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamTwo_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamTwo_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal one (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 0, 1, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamTwo_name, img))
            
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
    
            # insert teams to broker table in year
            sql_insert = f"INSERT IGNORE INTO {tabel_broker} VALUES (%s, %s)"
            for item in idTeams:
                mycursor.execute(sql_insert, (idLeague, item))
        case _:
            tabel_league_s = sport_name.lower() + "_leagues_season"
            tabel_league_y = sport_name.lower() + "_leagues_year"
            tabel_broker_s = sport_name.lower() + "_broker_season"
            tabel_broker_y = sport_name.lower() + "_broker_year"
            tabel_teams_s = sport_name.lower() + "_teams_season"
            tabel_teams_y = sport_name.lower() + "_teams_year"

            # checking if exist a league in year
            sql_league_check = f"SELECT * FROM {tabel_league_y} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_league_check, (league_name, User.user_id)) #execute function execute a sql query
            myresult_league_y = mycursor.fetchall() #getting a result to list
            # checking if exist a league in season
            sql_league_check = f"SELECT * FROM {tabel_league_s} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_league_check, (league_name, User.user_id)) #execute function execute a sql query
            myresult_league_s = mycursor.fetchall() #getting a result to list

            print(f"user: {User.user_id}") # check user id

            if myresult_league_y != []:
                sql_update_league = f"UPDATE {tabel_league_y} SET count = count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_league, (league_name, User.user_id))       
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of league image
                mycursor.execute(sql_img_search, (league_name,))
                img = mycursor.fetchall()

                # if don't exist league name then img equal one (basic image for league)
                if img == []:
                    img = 1
                else:
                    img = img[0]

                sql_insert_league = f"INSERT INTO {tabel_league_y} (id, id_user, name, count, img) VALUES (NULL, %s, %s, 1, %s)"
                mycursor.execute(sql_insert_league, (User.user_id, league_name, img))

            if myresult_league_s != []:
                sql_update_league = f"UPDATE {tabel_league_s} SET count = count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_league, (league_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of league image
                mycursor.execute(sql_img_search, (league_name,))
                img = mycursor.fetchall()

                # if don't exist league name then img equal one (basic image for league)
                if img == []:
                    img = 1
                else:
                    img = img[0]

                sql_insert_league = f"INSERT INTO {tabel_league_s} (id, id_user, name, count, img) VALUES (NULL, %s, %s, 1, %s)"
                mycursor.execute(sql_insert_league, (User.user_id, league_name, img))



            # checking if team one exist
            sql_team_one_check = f"SELECT * FROM {tabel_teams_y} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_one_check, (teamOne_name, User.user_id))
            myresult_team_one_y = mycursor.fetchall()
            sql_team_one_check = f"SELECT * FROM {tabel_teams_s} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_one_check, (teamOne_name, User.user_id))
            myresult_team_one_s = mycursor.fetchall()

            if myresult_team_one_y != []:
                sql_update_teamone = f"UPDATE {tabel_teams_y} SET home_count = home_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamOne_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamOne_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal two (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams_y} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 1, 0, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamOne_name, img))

            if myresult_team_one_s != []:
                sql_update_teamone = f"UPDATE {tabel_teams_s} SET home_count = home_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamOne_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamOne_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal two (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams_s} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 1, 0, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamOne_name, img))


            # checking if team two exist
            sql_team_two_check = f"SELECT * FROM {tabel_teams_y} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_two_check, (teamTwo_name, User.user_id))
            myresult_team_two_y = mycursor.fetchall()
            sql_team_two_check = f"SELECT * FROM {tabel_teams_s} WHERE name = %s AND id_user = %s"
            mycursor.execute(sql_team_two_check, (teamTwo_name, User.user_id))
            myresult_team_two_s = mycursor.fetchall()

            if myresult_team_two_y != []:
                sql_update_teamone = f"UPDATE {tabel_teams_y} SET away_count = away_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamTwo_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamTwo_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal one (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams_y} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 0, 1, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamTwo_name, img))

            if myresult_team_two_s != []:
                sql_update_teamone = f"UPDATE {tabel_teams_s} SET away_count = away_count + 1 WHERE name = %s AND id_user = %s"
                mycursor.execute(sql_update_teamone, (teamTwo_name, User.user_id))
            else:
                sql_img_search = f"SELECT id FROM images WHERE name = %s" # taking id of team image
                mycursor.execute(sql_img_search, (teamTwo_name,))
                img = mycursor.fetchall()

                # if don't exist team name then img equal one (basic image for team)
                if img == []:
                    img = 2
                else:
                    img = img[0]

                sql_insert_teamone = f"INSERT INTO {tabel_teams_s} (id, id_user, name, home_count, away_count, img) VALUES (NULL, %s, %s, 0, 1, %s)"
                mycursor.execute(sql_insert_teamone, (User.user_id, teamTwo_name, img))


            # taking id from league table
            sql_take_idleague = f"SELECT id FROM {tabel_league_y} WHERE name = %s"
            mycursor.execute(sql_take_idleague, (league_name,))
            result = mycursor.fetchone() # take first record
            idLeague_y = result[0] # take id
            print(idLeague_y)

            sql_take_idleague = f"SELECT id FROM {tabel_league_s} WHERE name = %s"
            mycursor.execute(sql_take_idleague, (league_name,))
            result = mycursor.fetchone() # take first record
            idLeague_s = result[0] # take id
            print(idLeague_s)

            # taking id for teams
            teams = [teamOne_name, teamTwo_name]
            idTeams_y = []
            print(teams)

            sql_take_idteam = f"SELECT id FROM {tabel_teams_y} WHERE name = %s"
            for item in teams:
                mycursor.execute(sql_take_idteam, (item,))
                result = mycursor.fetchone()

                idTeam = result[0]
                idTeams_y.append(idTeam)

            idTeams_s = []

            sql_take_idteam = f"SELECT id FROM {tabel_teams_s} WHERE name = %s"
            for item in teams:
                mycursor.execute(sql_take_idteam, (item,))
                result = mycursor.fetchone()

                idTeam = result[0]
                idTeams_s.append(idTeam)

            print(idTeams_y)
            print(idTeams_s)

            # insert teams to broker table in year
            sql_insert = f"INSERT IGNORE INTO {tabel_broker_y} VALUES (%s, %s)"
            for item in idTeams_y:
                    mycursor.execute(sql_insert, (idLeague_y, item))

            # inserting data to broker table in season
            sql_insert = f"INSERT IGNORE INTO {tabel_broker_s} VALUES (%s, %s)"
            for item in idTeams_s:
                    mycursor.execute(sql_insert, (idLeague_s, item))

    print(f"Added teams {teams[0]} and {teams[1]} to the competition {league_name}")

    connect.commit()
    connect.close()
    
def insert_user(name, mail, password):
    connect = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "database"
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
        sql_insert = "INSERT INTO users (id_users, mail, name, password) VALUES (NULL, %s, %s, %s)"
        mycursor.execute(sql_insert, (mail, name, hashed))

    connect.commit()
    connect.close()
    return True

def check_user(login, password):
    connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'database'
    )

    mycursor = connect.cursor()

    sql_check = "SELECT mail, name FROM users WHERE mail = %s or name = %s"
    mycursor.execute(sql_check, (login, login))
    myresult = mycursor.fetchall()

    if myresult != []:
        sql_pass_check = "SELECT password FROM users WHERE name = %s or mail = %s"
        mycursor.execute(sql_pass_check, (login, login))
        myresult = mycursor.fetchone()
        hash_pass = myresult[0].encode()
        
        if bcrypt.checkpw(password.encode(), hash_pass):
            sql_user_id = "SELECT id_users FROM users WHERE name = %s or mail = %s"
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