class Dollar():
    amount: int
    def __init__(self, amount: int) -> None:
        self.amount = amount
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dollar):
            return NotImplemented
        return self.amount == other.amount
    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self.amount * multiplier)


