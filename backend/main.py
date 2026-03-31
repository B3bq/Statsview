from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, insert, leagues, teams

app = FastAPI(title="Statsview API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(insert.router)
app.include_router(leagues.router)
app.include_router(teams.router)

@app.get("/")
def read_root():
    return {"message": "Statsview API is running"}
