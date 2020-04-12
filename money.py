class Money:
    _amount: int
    _currency: str

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency() != other.currency():
            return False
        return self._amount == other._amount

    @classmethod
    def dollar(cls, amount: int) -> 'Money':
        return Money(amount, 'USD')

    @classmethod
    def franc(cls, amount: int) -> 'Money':
        return Money(amount, 'CHF')

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)
