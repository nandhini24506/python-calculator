import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_returns_decimal_when_needed():
    assert divide(5, 2) == 2.5


def test_add_with_negative_number():
    assert add(-2, 5) == 3


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
