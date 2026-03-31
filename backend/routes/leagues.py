from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from db.connection import get_connection

router = APIRouter()

class LeagueRequest(BaseModel):
    sport: str
    user: Optional[int] = None
    season: Optional[str] = None

def take_leagues(db, table_league: str):
    with db.cursor() as cursor:
        try:
            cursor.execute(f"SELECT name FROM {table_league} ORDER BY name ASC")
            return cursor.fetchall()
        except Exception:
            return []

@router.post("/leagues/show-leagues")
def show_leagues(data: LeagueRequest):
    if not data.sport:
        raise HTTPException(status_code=400, detail="Missing sport")

    db = get_connection()
    try:
        if data.sport == "League of Legends":
            table_league = "lol_leagues"
            result = take_leagues(db, table_league)
        elif data.sport == "Counter Strike":
            table_league = "cs_leagues"
            result = take_leagues(db, table_league)
        else:
            sport_prefix = data.sport.lower()
            table_league = f"{sport_prefix}_leagues_season"
            result = take_leagues(db, table_league)
            
            if not result:
                table_league = f"{sport_prefix}_leagues_year"
                result = take_leagues(db, table_league)

        all_leagues = [row["name"] for row in result]
        return {"status": "ok", "data": all_leagues}
    finally:
        db.close()

@router.post("/leagues/top-leagues")
def top_leagues(data: LeagueRequest):
    if not data.sport:
        raise HTTPException(status_code=400, detail="Missing sport")

    db = get_connection()
    try:
        if data.sport in ["League of legends", "League of Legends"]:
            table_league = "lol_leagues"
        elif data.sport == "Counter Strike":
            table_league = "cs_leagues"
        else:
            sport_prefix = data.sport.lower()
            if data.season == "season":
                table_league = f"{sport_prefix}_leagues_season"
            else:
                table_league = f"{sport_prefix}_leagues_year"

        with db.cursor() as cursor:
            query = f"""
                SELECT {table_league}.name, {table_league}.count, images.img 
                FROM {table_league} 
                JOIN images ON {table_league}.img = images.id 
                WHERE id_user = %%s 
                ORDER BY count DESC LIMIT 5
            """
            cursor.execute(query, (data.user,))
            top_leagues_list = cursor.fetchall()

        return {"status": "ok", "data": top_leagues_list}
    finally:
        db.close()
