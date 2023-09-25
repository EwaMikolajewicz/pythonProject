from calculator import Calculator
import pytest


def test_add_positive():
    """doc"""
    assert Calculator.add(3, 4) == 7


def test_add_negative():
    """doc"""
    assert Calculator.add(-3, -4) == -7


def test_sub_positive():
    """doc"""
    assert Calculator.sub(3, 4) == -1


def test_sub_negative():
    """doc"""
    assert Calculator.sub(-3, -4) == 1


def test_mul_positive():
    """doc"""
    assert Calculator.mul(3, 4) == 12


def test_mul_negative():
    """doc"""
    assert Calculator.mul(-3, -4) == 12


def test_div_positive():
    """doc"""
    assert Calculator.div(3, 4) == 0.75


def test_div_positive0():
    """doc"""
    assert Calculator.div(3, 0) == "error: dzielenie przez zero"


def test_div_negative():
    """doc"""
    assert Calculator.div(-3, -4) == 0.75


def test_add_large():
    assert Calculator.add(200_000, 400_000) == 600_000


@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


def test_sum(sample_data):
    result = sum(sample_data)
    assert result == 15
