

def test_add(calculator):
    x, y = 3, 5
    z = calculator.add(x, y)
    assert z == x + y

def test_mul(calculator):
    x, y = 3, 5
    z = calculator.multiply(x, y)
    assert z == x * y
