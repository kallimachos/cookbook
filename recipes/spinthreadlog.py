#!/bin/python3
"""Example using logging_spinner, colorlog, asyncio, and aiohttp modules."""

import asyncio
import time

import aiohttp
import colorlog
import requests
from logging_spinner import SpinnerHandler, UserWaitingFilter

logger = colorlog.getLogger()


def sample_program(interval):
    """Do something."""
    logger.info("Processing", extra={"user_waiting": True})
    time.sleep(interval)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    try:
        x = 1 / 0
        logger.info("Still processing...", extra={"user_waiting": True})
        time.sleep(interval)
        print(x)
        logger.info("OK Processing complete.", extra={"user_waiting": False})
    except ZeroDivisionError:
        logger.critical("FAIL Processing failed.", extra={"user_waiting": False})
        logger.error("You tried to divide by zero.")
        raise


def serial_download_site(session, url):
    """Do something."""
    with session.get(url) as response:
        print(response)
    return


def serial_download_all_sites(sites):
    """Do something."""
    with requests.Session() as session:
        for url in sites:
            serial_download_site(session, url)


def run_serial(sites):
    """Do something."""
    start_time = time.time()
    serial_download_all_sites(sites)
    duration = time.time() - start_time
    return (len(sites), duration)


async def download_site(session, url):
    """Do something."""
    async with session.get(url) as response:
        if response.status != 200:
            logger.error("%s - %s" % (response.status, url))
        pass


async def download_all_sites(sites):
    """Do something."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def run_async(sites):
    """Do something."""
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    return (len(sites), duration)


def logconfig():
    """Do something."""
    handler = SpinnerHandler()
    logger.addHandler(handler)
    logger.setLevel("INFO")
    stream_handler = colorlog.StreamHandler()
    stream_handler.addFilter(UserWaitingFilter())
    stream_handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(asctime)s %(log_color)s%(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] "
            "%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(stream_handler)


if __name__ == "__main__":
    logconfig()
    # logger.setLevel("DEBUG")
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
        "http://www.jython.org/asdfgdfsaf",
    ] * 3
    logger.debug(sites)
    logger.info("Running serial", extra={"user_waiting": True})
    serial = run_serial(sites)
    print("Serial: %s sites in %s seconds" % serial)
    logger.info("Running async", extra={"user_waiting": True})
    time.sleep(2)
    unsync = run_async(sites)
    logger.info("Async:  %s sites in %s seconds" % unsync, extra={"user_waiting": False})
