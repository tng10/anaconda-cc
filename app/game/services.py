from sqlalchemy.orm import Session

from . import models
from .core import schema


def save_game(db: Session, game: schema.GameDb) -> models.Game | None:
    saved_game: models.Game | None = None
    db_game = get_game(db, game.id)
    if db_game:
        db_game.state = game.state
        saved_game = db_game
    else:
        saved_game = models.Game(id=game.id, state=game.state)

    db.add(saved_game)
    db.commit()
    db.refresh(saved_game)
    return saved_game


def get_game(db: Session, game_id: str) -> models.Game | None:
    game: models.Game | None = (
        db.query(models.Game).filter(models.Game.id == game_id).first()
    )
    return game
