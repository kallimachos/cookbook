#!/usr/bin/env python3
"""Compare threading, asyncio, and multiprocessing."""

import asyncio
import itertools
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import aiohttp
import requests

urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 10
n_jobs = len(urls)


def cpu_heavy(x):
    """Perform a CPU heavy task."""
    count = x
    for i in range(10**8):
        count += i
    return x


def cpu_serial(num):
    """Run serial."""
    result = []
    for x in range(num):
        result.append(cpu_heavy(x))
    return result


def cpu_multithreading(func, x, workers):
    """Run multithreaded."""
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, x)
    return list(res)


def cpu_multiprocessing(func, x, workers):
    """Run multiprocessed."""
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, x)
    return list(res)


def io_heavy(session, x):
    """Perform an IO heavy task."""
    with session.get(urls[x]) as response:
        return response


def io_serial(session) -> None:
    """Run serial."""
    for x in range(n_jobs):
        io_heavy(session, x)


def io_multithreading(func, session, x, workers):
    """Run multithreaded."""
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, session, x)
    return list(res)


def io_multiprocessing(func, session, x, workers):
    """Run multiprocessed."""
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, session, x)
    return list(res)


async def download_site(session, url):
    """Async download."""
    # async with session.get(url) as response:
    #     return response
    return await session.get(url)


async def download_all_sites(sites):
    """Async all downloads."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        await asyncio.gather(*tasks, return_exceptions=True)
    return tasks


def run_cpu_bound() -> None:
    """Run all CPU functions."""
    num = 2

    time.time()
    cpu_serial(num)

    time.time()
    cpu_multithreading(cpu_heavy, range(num), num)

    time.time()
    cpu_multiprocessing(cpu_heavy, range(num), num if num <= 4 else 4)


def run_io_bound() -> None:
    """Run all IO functions."""
    session = requests.Session()

    time.time()
    io_serial(session)

    time.time()
    io_multithreading(io_heavy, itertools.repeat(session), range(n_jobs), n_jobs)

    time.time()
    asyncio.run(download_all_sites(urls))

    time.time()
    io_multiprocessing(io_heavy, itertools.repeat(session), range(n_jobs), 4)


if __name__ == "__main__":
    # run_cpu_bound()
    run_io_bound()
