from money import Money, Bank

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

def test_simple_addition():
    sum: Expression = Money.dollar(4) + Money.dollar(1)
    bank = Bank()
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(5) == reduced
