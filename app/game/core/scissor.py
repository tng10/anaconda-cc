from app.game.core.element import Element, ElementComparable, ElementEnum


class Scissor(Element, ElementComparable):
    current: ElementEnum = ElementEnum.SCISSOR

    @property
    def name(self) -> str:
        return self.current.name

    @property
    def beats(self) -> ElementEnum:
        return ElementEnum.PAPER

    @property
    def beaten_by(self) -> ElementEnum:
        return ElementEnum.ROCK

    @property
    def draws_with(self) -> ElementEnum:
        return ElementEnum.SCISSOR
