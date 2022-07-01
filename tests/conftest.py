from calculator.Calculator import Calculator
import pytest


@pytest.fixture()
def calculator():
    calc = Calculator()
    yield calc
