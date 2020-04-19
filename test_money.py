import pytest # type: ignore

from money import Money, Bank

@pytest.fixture
def bank():
    mybank = Bank()
    mybank.add_rate("CHF", "USD", 2)
    return mybank

def test_that_tests_run():
    pass

def test_multiplication():
    five: Money

    five = Money.dollar(5)

    assert Money.dollar(10) == five * 2
    assert Money.dollar(15) == five * 3

def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) == Money.franc(5)
    assert Money.franc(5) != Money.franc(6)
    assert Money.dollar(5) != Money.franc(5)

def test_currency():
    assert "USD" == Money.dollar(5).currency()
    assert "CHF" == Money.franc(5).currency()

def test_simple_addition(bank):
    sum: Expression = Money.dollar(4) + Money.dollar(1)
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(5) == reduced

def test_reduce_sum(bank):
    sum: Expression = Money.dollar(9) + Money.dollar(2)
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(11) == reduced

def test_reduce_money(bank):
    reduced: Money = bank.reduce(Money.dollar(2), "USD")
    assert Money.dollar(2) == reduced

def test_reduce_money_with_conversion(bank):
    reduced: Money = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(4) == reduced

def test_reduction_doesnt_mutate(bank):
    reduced: Money = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(4) == reduced
    reduced: Money = bank.reduce(Money.franc(5), "USD")
    assert Money.dollar(10) == reduced

def test_add_two_currencies(bank):
    sum: Expression = Money.franc(2) + Money.dollar(10)
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(14) == reduced

def test_add_two_expressions(bank):
    sum: Expression = Money.franc(2) + Money.dollar(10)
    sum += Money.dollar(3)
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(17) == reduced

def test_multiply_expressions(bank):
    sum: Expression = Money.franc(2) + Money.dollar(10)
    sum *= 2
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(28) == reduced

