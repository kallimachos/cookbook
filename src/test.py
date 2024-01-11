#!/bin/python3
"""Pytest and hypothesis examples.

Run using 'pytest test.py'
"""

import pytest
from hypothesis import given
from hypothesis.strategies import integers, text


# Functions to be tested.
def add(x):
    """Return x +1.

    >>> add(2)
    3
    """
    return x + 1


def square(x):
    """Square x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x * x


def mystring(s):
    """Return s."""
    return s + s


# Test using hypothesis data generation


@given(integers())
def test_add_h(i) -> None:
    """Test add."""
    assert add(i) == i + 1


@given(integers())
def test_square_h(i) -> None:
    """Test square."""
    assert square(i) == i * i


@given(text())
def test_mystring_h(s) -> None:
    """Test string."""
    x = mystring(s)
    assert x == s + s


# Test using pytest parameters


@pytest.mark.parametrize(
    "value, result",
    [(1, 2), (2, 3), (3, 4)],
)
def test_add_p(value, result) -> None:
    """Test add."""
    assert add(value) == result


@pytest.mark.parametrize(
    "value, result",
    [(1, 1), (2, 4), (3, 9)],
)
def test_square_p(value, result) -> None:
    """Test add."""
    assert square(value) == result


@pytest.mark.parametrize(
    "value, result",
    [("hi", "hihi"), ("bye", "byebye")],
)
def test_mystring_p(value, result) -> None:
    """Test add."""
    assert mystring(value) == result
