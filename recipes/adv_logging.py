#!/bin/python3
"""Example usage of the logging module with a configuration file."""

import logging
import logging.config

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


if __name__ == '__main__':
    # load conf file
    logging.config.fileConfig('log.conf')

    # create logger
    logger = logging.getLogger('simpleExample')

    # invoke logging in code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
