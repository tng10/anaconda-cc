from app.game.core.play import Play
from app.game.core.player import Player


class GameHistory:

    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1: Player = player1
        self.player2: Player = player2
        self.actions: list[Play] = []

    def add(self, play: Play) -> None:
        self.actions.append(play)
