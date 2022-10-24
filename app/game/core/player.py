from dataclasses import dataclass
from random import choice

from app.game.core.element import ElementEnum


@dataclass
class Player:
    name: str
    is_human: bool

    def __repr__(self) -> str:
        return f'{self.name}'

    def choice(self) -> ElementEnum:
        chosen = choice([element for element in ElementEnum])
        print(f'{self.name} has chosen {chosen.value}')
        return chosen
