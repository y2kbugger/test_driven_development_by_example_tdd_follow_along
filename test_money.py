from money import Dollar

def test_that_tests_run():
    pass

def testMultiplication():
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount
    five.times(3)
    assert 30 == five.amount
