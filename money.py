from typing import cast

class Expression:
    def reduce(self, to: str):
        raise NotImplementedError()

class Money(Expression):
    _amount: int
    _currency: str
    def __repr__(self):
        return f"{self._amount}{self._currency}"

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency() != other.currency():
            return False
        return self._amount == other._amount

    def __add__(self, addend) -> 'Expression':
        return Sum(self, addend)

    def __mul__(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, 'CHF')

    def currency(self) -> str:
        return self._currency

    def reduce(self, to: str) -> 'Money':
        return self

class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.addend = addend
        self.augend = augend
    def reduce(self, to: str) -> Money:
        return Money(self.augend._amount + self.addend._amount, to)

class Bank:
    def reduce(self, ex: Expression, to: str) -> Money:
        return ex.reduce(to)
