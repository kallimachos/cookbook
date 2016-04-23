#!/bin/python3
"""Basic example using the logging module."""

import logging
from os import path, remove

# Log levels
# DEBUG    Detailed information, typically of interest only when diagnosing
#          problems.
# INFO 	   Confirmation that things are working as expected.
# WARNING  An indication that something unexpected happened, or indicative of
#          some problem in the near future (e.g. disk space low). The software
#          is still working as expected.
# ERROR    Due to a more serious problem, the software has not been able to
#          perform some function.
# CRITICAL A serious error, indicating that the program itself may be unable to
#          continue running.


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='example.log',
                    filemode='w')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')

message = 'variables'
number = 5
logging.critical('This is a critical message about %s using %s',
                 number, message)


def test_cleanup():
    """Remove example.log file."""
    if path.exists('example.log'):
        remove('example.log')
    assert True is True
