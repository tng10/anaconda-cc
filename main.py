from fastapi import FastAPI
from app.game import router as game_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(game_router.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def main():
    return {"message": "FastAPI"}
