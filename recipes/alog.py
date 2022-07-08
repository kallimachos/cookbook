#!/bin/python3
"""Basic example using structlog."""

import requests
import slog
import structlog
import tlog

logger = structlog.get_logger()


def trial():
    """Run examples."""
    tlog.trial()
    logger.debug("alog debug message")
    logger.info("alog info message")
    logger.warning("alog warning message")
    logger.error("alog error message")
    logger.critical("alog critical message")
    try:
        assert True is False
    except AssertionError:
        logger.exception("This is an exception message")
    requests.get("http://www.google.com")


if __name__ == "__main__":
    slog.logconfig(console=False, debug=True)
    trial()
