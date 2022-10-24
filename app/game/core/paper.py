from app.game.core.element import Element, ElementComparable, ElementEnum


class Paper(Element, ElementComparable):
    current: ElementEnum = ElementEnum.PAPER

    @property
    def name(self) -> str:
        return self.current.name

    @property
    def beats(self) -> ElementEnum:
        return ElementEnum.ROCK

    @property
    def beaten_by(self) -> ElementEnum:
        return ElementEnum.SCISSOR
        
    @property
    def draws_with(self) -> ElementEnum:
        return ElementEnum.PAPER
