#!/bin/python3
"""Demonstrate use of sh module."""

import sh


def echo():
    """Use sh module to run bash echo command."""
    return(sh.echo('hello'))


def test_echo():
    """Test echo function."""
    result = echo()
    assert result == 'hello\n'


if __name__ == '__main__':
    print(sh.ls('.'))
