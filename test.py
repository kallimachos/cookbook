#!/bin/python3

#===========================================================
# Testing
#
# Run using 'py.test pytest.py'
#
#-----------------------------------------------------------
# Functions to be tested

def func(x):
    return x + 1

def mystring():
    return 'This is a string.'

#----------------------------------------------------------
# Tests in pytest format.

def test_answer():
    assert func(3) == 4

def test_string():
    x = mystring()
    assert isinstance(x, basestring)

def test_less_than():
    assert 4 < 5

def test_greater_than():
    assert 4 > 5

def test_repeat():
    for x in range(10):
        assert x != 11