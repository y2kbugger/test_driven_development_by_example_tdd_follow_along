from money import Money

def test_that_tests_run():
    pass

def test_multiplication():
    five: Money

    five = Money.dollar(5)

    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)

def test_franc_multiplication():
    five: Money

    five = Money.franc(5)

    assert Money.franc(10) == five.times(2)
    assert Money.franc(15) == five.times(3)

def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) == Money.franc(5)
    assert Money.franc(5) != Money.franc(6)
    assert Money.dollar(5) != Money.franc(5)

def test_currency():
    assert "USD" == Money.dollar(5).currency()
    assert "CHF" == Money.franc(5).currency()
