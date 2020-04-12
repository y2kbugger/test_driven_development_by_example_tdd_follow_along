class Money:
    amount: int
    def __init__(self, amount: int) -> None:
        self._amount = amount
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        if self.__class__ != other.__class__:
            return False
        return self._amount == other._amount

class Dollar(Money):
    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)

class Franc(Money):
    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)

