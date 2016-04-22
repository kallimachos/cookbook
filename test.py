#!/bin/python3
"""
Pytest examples.

Run using 'py.test pytest.py'
"""

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


def mystring():
    """Return This is a string."""
    return 'This is a string.'


# Tests in pytest format.

def test_add():
    """Test add."""
    assert add(3) == 4


def test_square():
    """Test square."""
    assert square(5) == 25


def test_mystring():
    """Test string."""
    x = mystring()
    assert isinstance(x, str)


def test_less_than():
    """Test a less than equation."""
    assert 4 < 5


def test_repeat():
    """Test using a for loop."""
    for x in range(10):
        assert x != 11
