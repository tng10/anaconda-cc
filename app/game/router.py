import logging

from fastapi import APIRouter, status, Request, Response, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.game import models
from app.game import services
from app.game.core.game import Game
from app.game.core.player import Player
from app.game.core.schema import GameDb
from app.game.schema import GamePlay, GameStart
from app.database import get_db


router = APIRouter(tags=["Game"], prefix="/game")

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


@router.post("/start", status_code=status.HTTP_201_CREATED)
async def start(
    req: GameStart, res: Response, db: Session = Depends(get_db)
) -> JSONResponse:

    p1: Player = Player(name=req.player1_name, is_human=req.player1_is_human)
    p2: Player = Player(name=req.player2_name, is_human=req.player2_is_human)
    game = Game(p1, p2)

    try:
        services.save_game(db, GameDb(id=game.id, state=game.serialize()))
    except Exception as err:
        logger.error(str(err))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not start the game !"
        )

    return JSONResponse(
        {
            "id": game.id,
            "player1": str(game.player1),
            "player2": str(game.player2),
            "player1_is_human": game.player1.is_human,
            "player2_is_human": game.player2.is_human,
            "turn": str(game.current_turn),
            "last_played": str(game.last_played) if game.last_played else None,
            "winner": str(game.winner) if game.winner else None,
        }
    )


@router.get("/resume/{game_id}", status_code=status.HTTP_200_OK)
async def game(
    game_id: str, req: Request, res: Response, db: Session = Depends(get_db)
) -> JSONResponse:
    game_db: models.Game | None = services.get_game(db, game_id)
    if not game_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !"
        )

    game: Game = Game.deserialize(game_db.state)

    return JSONResponse(
        {
            "id": game.id,
            "player1": str(game.player1),
            "player2": str(game.player2),
            "player1_is_human": game.player1.is_human,
            "player2_is_human": game.player2.is_human,
            "turn": str(game.current_turn),
            "last_played": str(game.last_played) if game.last_played else None,
            "winner": str(game.winner) if game.winner else None,
        }
    )


@router.put("/play/{game_id}", status_code=status.HTTP_200_OK)
async def play(
    game_id: str, req: GamePlay, res: Response, db: Session = Depends(get_db)
) -> JSONResponse:
    game_db: models.Game | None = services.get_game(db, game_id)

    if not game_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !"
        )

    game: Game = Game.deserialize(game_db.state)

    # play
    game.play(req)

    # evaluate
    if game.current_play.is_complete:
        game.evaluate()

    # persist
    try:
        services.save_game(db, GameDb(id=game.id, state=game.serialize()))
    except Exception as err:
        logger.error(str(err))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Could not start the game !"
        )

    return JSONResponse(
        {
            "id": game.id,
            "player1": str(game.player1),
            "player2": str(game.player2),
            "player1_is_human": game.player1.is_human,
            "player2_is_human": game.player2.is_human,
            "turn": str(game.current_turn),
            "last_played": str(game.last_played) if game.last_played else None,
            "winner": str(game.winner) if game.winner else None,
        }
    )
