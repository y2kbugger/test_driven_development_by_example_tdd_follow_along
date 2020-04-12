class Dollar():
    amount: int
    def __init__(self, amount: int) -> None:
        self._amount = amount
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dollar):
            return NotImplemented
        return self._amount == other._amount
    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)

class Franc():
    amount: int
    def __init__(self, amount: int) -> None:
        self._amount = amount
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Franc):
            return NotImplemented
        return self._amount == other._amount
    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)

