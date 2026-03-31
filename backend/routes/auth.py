from fastapi import APIRouter
from pydantic import BaseModel
from db import get_connection
import bcrypt

router = APIRouter()

class LoginData(BaseModel):
    login: str
    password: str

class RegisterData(BaseModel):
    name: str
    mail: str
    hashed: str

class NameCheck(BaseModel):
    name: str


@router.post("/auth/check-name")
def check_name(data: NameCheck):
    db = get_connection()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name=%s", (data.name,))
        res = cursor.fetchone()

    return {"success": res is None}


@router.post("/auth/login")
def login(data: LoginData):
    db = get_connection()

    with db.cursor() as cursor:
        cursor.execute(
            "SELECT id_users, password FROM users WHERE mail=%s OR name=%s",
            (data.login, data.login)
        )
        user = cursor.fetchone()

    if not user:
        return {"success": False, "text": "User don't exist"}

    if bcrypt.checkpw(data.password.encode(), user["password"].encode()):
        return {"success": True, "id_user": user["id_users"]}
    else:
        return {"success": False, "text": "Incorrect password"}


@router.post("/auth/register")
def register(data: RegisterData):
    db = get_connection()

    with db.cursor() as cursor:
        cursor.execute("SELECT id_users FROM users WHERE name=%s", (data.name,))
        if cursor.fetchone():
            return {"success": False}

        cursor.execute(
            "INSERT INTO users (mail, name, password, photo) VALUES (%s, %s, %s, 'src/img/user.png')",
            (data.mail, data.name, data.hashed)
        )
        db.commit()

    return {"success": True}