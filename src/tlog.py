#!/bin/python3
"""Basic example using structlog."""

import requests
import slog
import structlog

logger = structlog.get_logger()


def trial() -> None:
    """Run examples."""
    logger.debug("tlog debug message")
    logger.info("tlog info message")
    logger.warning("tlog warning message")
    logger.error("tlog error message")
    logger.critical("tlog critical message")
    try:
        assert True is False
    except AssertionError:
        logger.exception("This is an exception message")
    requests.get("http://www.google.com")


if __name__ == "__main__":
    slog.logconfig(console=True, debug=False)
    trial()
