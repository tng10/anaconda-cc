from pydantic import BaseModel


class GameState(BaseModel):
    id: str
    player1: str
    player2: str
    player1_is_human: bool
    player2_is_human: bool
    turn: str
    last_played: str | None
    winner: str | None


class GameDb(BaseModel):
    id: str
    state: str

    class Config:
        orm_mode = True
