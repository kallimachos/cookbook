#!/bin/python3
"""
Pytest and hypothesis examples.

Run using 'py.test pytest.py'
"""

from hypothesis import given
from hypothesis.strategies import integers, text


# Functions to be tested.
def add(x):
    """
    Return x +1.

    >>> add(2)
    3
    """
    return x + 1


def square(x):
    """
    Square x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x * x


def mystring(s):
    """Return s."""
    return s


# Tests in pytest format using hypothesis data generation


@given(integers())
def test_add(i):
    """Test add."""
    assert add(i) == i + 1


@given(integers())
def test_square(i):
    """Test square."""
    assert square(i) == i * i


@given(text())
def test_mystring(s):
    """Test string."""
    x = mystring(s)
    assert isinstance(x, str)


def test_less_than():
    """Test a less than equation."""
    assert 2 < 5


def test_repeat():
    """Test using a for loop."""
    for x in range(10):
        assert x != 11
