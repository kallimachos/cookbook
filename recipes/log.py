#!/bin/python3
"""Basic example using the logging module."""

import colorlog

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

logger = colorlog.getLogger()


def logconfig(level="INFO"):
    """Set logging configuration.

    Args:
        level (str, optional): log level to use

    """
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(asctime)s %(log_color)s%(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] "
            "%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    return logger.level


if __name__ == "__main__":
    logconfig("DEBUG")
