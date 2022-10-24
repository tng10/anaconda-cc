import pickle
from uuid import uuid4
from app.game.core.element import ElementEnum
from app.game.core.history import GameHistory
from app.game.core.paper import Paper
from app.game.core.play import Play
from app.game.core.player import Player
from app.game.core.rock import Rock
from app.game.core.scissor import Scissor
from app.game.schema import GamePlay


class Game:
    def __init__(self, player1: Player, player2: Player | None = None) -> None:
        self.id = str(uuid4())
        self.player1 = player1
        self.player2 = player2 if player2 else Player("Machine", False)
        self.history = GameHistory(self.player1, self.player2)
        self.winner: Player | None = None
        self.current_turn: Player = self.player1
        self.current_play: Play = Play(choice1=None, choice2=None)

    @property
    def actions(self):
        return {
            ElementEnum.ROCK.name: Rock(),
            ElementEnum.PAPER.name: Paper(),
            ElementEnum.SCISSOR.name: Scissor(),
        }

    def evaluate(self) -> None:
        choice1_name = None
        choice2_name = None
        if self.current_play.choice1 and self.current_play.choice2:
            choice1_name = self.current_play.choice1.name
            choice2_name = self.current_play.choice2.name

        self.history.add(self.current_play)
        if self.actions[choice1_name] > self.actions[choice2_name]:
            self.winner = self.player1
        elif self.actions[choice1_name] < self.actions[choice2_name]:
            self.winner = self.player2
        else:
            self.winner = None
            self.current_play = Play(choice1=None, choice2=None)

    def play(self, request: GamePlay | None = None) -> None:

        if self.current_turn == self.player1:
            if (
                request
                and self.current_turn.name == request.current_turn
                and request.choice
            ):
                self.current_play.choice1 = request.choice
            else:
                self.current_play.choice1 = self.player1.choice()
            self.current_turn = self.player2

        elif self.current_turn == self.player2:
            if (
                request
                and self.current_turn.name == request.current_turn
                and request.choice
            ):
                self.current_play.choice2 = request.choice
            else:
                self.current_play.choice2 = self.player2.choice()
            self.current_turn = self.player1

        if not request or not self.player2.is_human:
            while not self.current_play.is_complete:
                self.play()

    @property
    def last_played(self):
        if self.history.actions:
            return self.history.actions[-1]
        return None

    def serialize(self):
        serialized_game = pickle.dumps(self, 0)
        return serialized_game.decode()

    @staticmethod
    def deserialize(state: str) -> "Game":
        game: "Game" = pickle.loads(str.encode(state))
        return game
