from typing import cast

class Expression:
    def __add__(self, addend: 'Expression') -> 'Expression':
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str):
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

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        bank.reduce(self, to)
        return self

class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression):
        self.addend = addend
        self.augend = augend
    def reduce(self, bank: 'Bank', to: str) -> Money:
        addend = bank.reduce(self.addend, to)
        augend = bank.reduce(self.augend, to)
        return Money(augend._amount + addend._amount, to)

class Bank:
    def __init__(self):
        self.rates: Dict[Tuple[str,str], float]= {}

    def _convert(self, money: Money, to):
        rate = self.rates[(money.currency(), to)]
        print(to)
        return Money(money._amount * rate, to)

    def reduce(self, ex: Expression, to: str) -> 'Money':
        if isinstance(ex, Money):
            return self._convert(ex, to)
        else:
            return ex.reduce(self, to)

    def add_rate(self, from_c: str, to_c: str, rate: int):
        assert from_c != to_c
        self.rates[(from_c, to_c)] = rate
        self.rates[(to_c, from_c)] = 1 / rate
        self.rates[(from_c, from_c)] = 1
        self.rates[(to_c, to_c)] = 1
