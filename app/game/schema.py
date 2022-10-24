from pydantic import BaseModel, Field, validator

from app.game.core.element import ElementEnum


class GameStart(BaseModel):
    player1_name: str = Field(min_length=1, max_length=128)
    player2_name: str = Field(min_length=1, max_length=128)
    player1_is_human: bool = Field(default=True)
    player2_is_human: bool = Field(default=True)


class GamePlay(BaseModel):
    current_turn: str = Field(min_length=1, max_length=128)
    choice: ElementEnum = Field(default=None)
