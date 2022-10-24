from dataclasses import dataclass
from app.game.core.element import ElementEnum


@dataclass
class Play:
    choice1: ElementEnum | None
    choice2: ElementEnum | None

    def __repr__(self) -> str:
        return f"{self.choice1.value if self.choice1 else 'None'} vs {self.choice2.value if self.choice2 else 'None'}"

    @property
    def is_complete(self):
        return self.choice1 is not None and self.choice2 is not None
