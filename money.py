class Money:
    _amount: int
    _currency: str

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        if self.__class__ != other.__class__:
            return False
        return self._amount == other._amount

    @classmethod
    def dollar(cls, amount: int) -> 'Money':
        return Dollar(amount, 'USD')

    @classmethod
    def franc(cls, amount: int) -> 'Money':
        return Franc(amount, 'CHF')

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> 'Money':
        raise NotImplementedError()

class Dollar(Money):
    _currency: str = 'USD'
    def times(self, multiplier: int) -> 'Money':
        return Money.dollar(self._amount * multiplier)

class Franc(Money):
    _currency: str = 'CHF'
    def times(self, multiplier: int) -> 'Money':
        return Money.franc(self._amount * multiplier)


