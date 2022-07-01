

def test_add(calculator):
    x, y = 3, 5
    z = calculator.add(x, y)
    assert z == x + y
