import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class TestMathOperations:
    def test_addition(self):
        assert 2 + 2 == 4
        assert 0 + 0 == 0
        assert -1 + 1 == 0

    def test_subtraction(self):
        assert 5 - 3 == 2
        assert 0 - 0 == 0
        assert 10 - 15 == -5

    def test_multiplication(self):
        assert 2 * 3 == 6
        assert 0 * 5 == 0
        assert -2 * 3 == -6

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_division_scenarios(self):
        assert divide(10, 2) == 5
        assert divide(0, 5) == 0
        assert divide(-10, 2) == -5