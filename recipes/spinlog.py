# #!/bin/python3
# """Example using the logging_spinner and colorlog modules."""
#
import sys
import time

import colorlog
from logging_spinner import SpinnerHandler, UserWaitingFilter

logger = colorlog.getLogger()


def sample_program(interval):
    failure = True
    logger.info("Processing", extra={"user_waiting": True})
    time.sleep(interval)  # Some time-taking process
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    try:
        x = 1 / 0
        logger.info("Still processing...", extra={"user_waiting": True})
        time.sleep(interval)
        logger.info("OK Processing complete.", extra={"user_waiting": False})
    except ZeroDivisionError as e:
        logger.critical("FAIL Processing failed.", extra={"user_waiting": False})
        logger.error("You tried to divide by zero.")
        raise


def main():
    interval = 3

    # Setup a SpinnerHandler to application logger(s)
    handler = SpinnerHandler()  # stream=sys.stdout)
    logger.addHandler(handler)
    logger.setLevel("INFO")

    # If a StreamHandler is also installed together it should filter
    # log records with "user_waiting" extra field so that these log messages
    # won't be printed twice (with a spinner, and without a spinner again).

    stream_handler = colorlog.StreamHandler()  # stream=stream)
    stream_handler.addFilter(UserWaitingFilter())
    # stream_handler.setLevel("DEBUG")
    stream_handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(asctime)s %(log_color)s%(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(stream_handler)
    # logger.setLevel("DEBUG")

    sample_program(interval=interval)


if __name__ == "__main__":
    main()
