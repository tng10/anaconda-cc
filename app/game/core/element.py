from enum import Enum
from abc import ABC, abstractproperty


class ElementEnum(Enum):
    ROCK: str = 'rock'
    PAPER: str = 'paper'
    SCISSOR: str = 'scissor'


class ElementComparable:

    def __eq__(self, other: object) -> bool:
        assert hasattr(other, 'current')
        assert hasattr(other, 'name')
        return self.draws_with == other.current # type: ignore
    
    def __lt__(self, other: object) -> bool:
        assert hasattr(other, 'current')
        assert hasattr(other, 'name')
        return self.beaten_by == other.current # type: ignore
        
    def __gt__(self, other: object) -> bool:
        assert hasattr(other, 'current')
        assert hasattr(other, 'name')
        return self.beats == other.current # type: ignore


class Element(ABC):
    current: ElementEnum
    
    @abstractproperty
    def name(self) -> str:
        pass

    @abstractproperty
    def beats(self) -> ElementEnum:
        pass
    
    @abstractproperty
    def beaten_by(self) -> ElementEnum:
        pass

    @abstractproperty
    def draws_with(self) -> ElementEnum:
        pass
