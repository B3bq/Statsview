from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from db.connection import get_connection

router = APIRouter()

class InsertData(BaseModel):
    sport: str
    league: str
    first: str
    second: str
    user: int

def img_search(db, variable: str, team_or_league: str) -> int:
    with db.cursor() as cursor:
        cursor.execute("SELECT id FROM images WHERE name = %s", (variable,))
        row = cursor.fetchone()
    
    img_id = row["id"] if row else None
    
    if team_or_league == "league":
        return int(img_id) if img_id is not None else 1
    else:
        return int(img_id) if img_id is not None else 2

def add_data(db, league: str, first_team: str, second_team: str, user_id: int, table_leagues: str, table_teams: str, table_broker: str):
    with db.cursor() as cursor:
        # Check and update/insert League
        cursor.execute(f"SELECT * FROM {table_leagues} WHERE name = %s AND id_user = %s", (league, user_id))
        if cursor.rowcount > 0:
            cursor.execute(f"UPDATE {table_leagues} SET count = count + 1 WHERE name = %s AND id_user = %s", (league, user_id))
        else:
            img = img_search(db, league, "league")
            cursor.execute(f"INSERT INTO {table_leagues} (id_user, name, count, img) VALUES (%s, %s, 1, %s)", (user_id, league, img))

        # Check and update/insert First Team
        cursor.execute(f"SELECT * FROM {table_teams} WHERE name = %s AND id_user = %s", (first_team, user_id))
        if cursor.rowcount > 0:
            cursor.execute(f"UPDATE {table_teams} SET home_count = home_count + 1 WHERE name = %s AND id_user = %s", (first_team, user_id))
        else:
            img = img_search(db, first_team, "team")
            cursor.execute(f"INSERT INTO {table_teams} (id_user, name, home_count, away_count, img) VALUES (%s, %s, 1, 0, %s)", (user_id, first_team, img))
            
        # Check and update/insert Second Team
        cursor.execute(f"SELECT * FROM {table_teams} WHERE name = %s AND id_user = %s", (second_team, user_id))
        if cursor.rowcount > 0:
            cursor.execute(f"UPDATE {table_teams} SET away_count = away_count + 1 WHERE name = %s AND id_user = %s", (second_team, user_id))
        else:
            img = img_search(db, second_team, "team")
            cursor.execute(f"INSERT INTO {table_teams} (id_user, name, home_count, away_count, img) VALUES (%s, %s, 0, 1, %s)", (user_id, second_team, img))

        # Get League ID
        cursor.execute(f"SELECT id FROM {table_leagues} WHERE name = %s AND id_user = %s", (league, user_id))
        league_row = cursor.fetchone()
        if league_row:
            league_id = league_row["id"]
        else:
            # Fallback grab
            cursor.execute(f"SELECT id FROM {table_leagues} WHERE name = %s", (league,))
            league_row_fallback = cursor.fetchone()
            league_id = league_row_fallback["id"] if league_row_fallback else 1

        teams = [first_team, second_team]
        team_ids = []
        for team in teams:
            cursor.execute(f"SELECT id FROM {table_teams} WHERE name = %s AND id_user = %s", (team, user_id))
            team_row = cursor.fetchone()
            if team_row:
                team_ids.append(team_row["id"])
            else:
                cursor.execute(f"SELECT id FROM {table_teams} WHERE name = %s", (team,))
                fallback_row = cursor.fetchone()
                if fallback_row:
                    team_ids.append(fallback_row["id"])

        for team_id in team_ids:
            cursor.execute(f"INSERT IGNORE INTO {table_broker} (id_league, id_team) VALUES (%s, %s)", (league_id, team_id))

    db.commit()


@router.post("/insert/insert-data")
def insert_data(data: InsertData):
    if not data.sport or not data.league or not data.first or not data.second or not data.user:
        raise HTTPException(status_code=400, detail="Invalid data")

    db = get_connection()
    try:
        if data.sport == "League of Legends":
            add_data(db, data.league, data.first, data.second, data.user, "lol_leagues", "lol_teams", "lol_broker")
        elif data.sport == "Counter Strike":
            add_data(db, data.league, data.first, data.second, data.user, "cs_leagues", "cs_teams", "cs_broker")
        else:
            sport_prefix = data.sport.lower()
            season_league = f"{sport_prefix}_league_season"
            season_team = f"{sport_prefix}_teams_season"
            season_broker = f"{sport_prefix}_broker_season"
            
            year_league = f"{sport_prefix}_league_year"
            year_team = f"{sport_prefix}_teams_year"
            year_broker = f"{sport_prefix}_broker_year"
            
            add_data(db, data.league, data.first, data.second, data.user, season_league, season_team, season_broker)
            add_data(db, data.league, data.first, data.second, data.user, year_league, year_team, year_broker)
        return {"success": True}
    finally:
        db.close()
