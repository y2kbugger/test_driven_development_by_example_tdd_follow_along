class Dollar():
    amount: int
    def __init__(self, amount: int) -> None:
        self.amount = amount
    def times(self, multiplier: int) -> None:
        self.amount *= multiplier

