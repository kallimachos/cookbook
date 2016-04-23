#!/bin/python3
"""Demonstrate use of sh module."""

import sh


def echo():
    """Use sh module to run bash echo command."""
    return(sh.echo('hello'))


def test_echo():
    """Test echo function."""
    assert echo() == 'hello'


if __name__ == '__main__':
    print(sh.ls('.'))
