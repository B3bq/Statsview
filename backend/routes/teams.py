from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from db.connection import get_connection

router = APIRouter()

class TeamRequest(BaseModel):
    sport: str
    league: Optional[str] = None
    user: Optional[int] = None
    season: Optional[str] = None

def take_teams(db, league: Optional[str], table_league: str, table_team: str, table_broker: str):
    with db.cursor() as cursor:
        try:
            query = f"""
                SELECT {table_team}.name 
                FROM {table_team} 
                JOIN {table_broker} ON {table_team}.id = {table_broker}.id_team 
                JOIN {table_league} ON {table_broker}.id_league = {table_league}.id 
                WHERE {table_league}.name = %%s 
                ORDER BY {table_team}.name ASC
            """
            cursor.execute(query, (league,))
            return cursor.fetchall()
        except Exception:
            return []

@router.post("/teams/show-teams")
def show_teams(data: TeamRequest):
    if not data.sport:
        raise HTTPException(status_code=400, detail="Missing sport")

    db = get_connection()
    try:
        sport = data.sport
        league = data.league
        
        if sport in ["League of legends", "League of Legends"]:
            table_league = "lol_leagues"
            table_team = "lol_teams"
            table_broker = "lol_broker"
            result = take_teams(db, league, table_league, table_team, table_broker)
        elif sport == "Counter Strike":
            table_league = "cs_leagues"
            table_team = "cs_teams"
            table_broker = "cs_broker"
            result = take_teams(db, league, table_league, table_team, table_broker)
        else:
            sport_prefix = sport.lower()
            table_league = f"{sport_prefix}_leagues_season"
            table_team = f"{sport_prefix}_teams_season"
            table_broker = f"{sport_prefix}_broker_season"

            result = take_teams(db, league, table_league, table_team, table_broker)
            if not result:
                table_league = f"{sport_prefix}_league_year"
                table_team = f"{sport_prefix}_teams_year"
                table_broker = f"{sport_prefix}_broker_year"
                result = take_teams(db, league, table_league, table_team, table_broker)

        teams_names = [row["name"] for row in result]
        return {"status": "ok", "data": teams_names}
    finally:
        db.close()

@router.post("/teams/top-teams")
def top_teams(data: TeamRequest):
    if not data.sport:
        raise HTTPException(status_code=400, detail="Missing sport")

    db = get_connection()
    try:
        sport = data.sport
        user_id = data.user
        season = data.season

        if sport in ["League of legends", "League of Legends"]:
            table_team = "lol_teams"
        elif sport == "Counter Strike":
            table_team = "cs_teams"
        else:
            sport_prefix = sport.lower()
            if season == 'season':
                table_team = f"{sport_prefix}_teams_season"
            else:
                table_team = f"{sport_prefix}_teams_years"

        with db.cursor() as cursor:
            query = f"""
                SELECT {table_team}.name, (home_count+away_count) AS total_count, images.img 
                FROM {table_team} 
                JOIN images ON {table_team}.img = images.id 
                WHERE id_user = %%s 
                ORDER BY total_count DESC LIMIT 5
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()

        return {"status": "ok", "data": result}
    finally:
        db.close()

@router.post("/teams/home-team")
def home_team(data: TeamRequest):
    if not data.sport:
        raise HTTPException(status_code=400, detail="Missing sport")

    db = get_connection()
    try:
        sport = data.sport
        user_id = data.user
        season = data.season

        if sport in ["League of legends", "League of Legends"]:
            table_team = "lol_teams"
        elif sport == "Counter Strike":
            table_team = "cs_teams"
        else:
            sport_prefix = sport.lower()
            if season == 'season':
                table_team = f"{sport_prefix}_teams_season"
            else:
                table_team = f"{sport_prefix}_teams_years"

        with db.cursor() as cursor:
            query = f"""
                SELECT {table_team}.name, home_count, images.img 
                FROM {table_team} 
                JOIN images ON {table_team}.img = images.id 
                WHERE id_user = %%s 
                ORDER BY home_count DESC LIMIT 1
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

        return {"status": "ok", "data": result}
    finally:
        db.close()

@router.post("/teams/away-team")
def away_team(data: TeamRequest):
    if not data.sport:
        raise HTTPException(status_code=400, detail="Missing sport")

    db = get_connection()
    try:
        sport = data.sport
        user_id = data.user
        season = data.season

        if sport in ["League of legends", "League of Legends"]:
            table_team = "lol_teams"
        elif sport == "Counter Strike":
            table_team = "cs_teams"
        else:
            sport_prefix = sport.lower()
            if season == 'season':
                table_team = f"{sport_prefix}_teams_season"
            else:
                table_team = f"{sport_prefix}_teams_years"

        with db.cursor() as cursor:
            query = f"""
                SELECT {table_team}.name, away_count, images.img 
                FROM {table_team} 
                JOIN images ON {table_team}.img = images.id 
                WHERE id_user = %%s 
                ORDER BY away_count DESC LIMIT 1
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

        return {"status": "ok", "data": result}
    finally:
        db.close()
