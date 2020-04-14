#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare threading, asyncio, and multiprocessing."""

import asyncio
import itertools
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import aiohttp
import requests


def cpu_heavy(x):
    """Perform a CPU heavy task."""
    count = x
    for i in range(10 ** 8):
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


def io_serial(session):
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
    response = await session.get(url)
    return response


async def download_all_sites(sites):
    """Async all downloads."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        await asyncio.gather(*tasks, return_exceptions=True)
    return tasks


def run_cpu_bound():
    """Run all CPU functions."""
    print("\n---------\ncpu heavy\n---------")
    num = 2

    start = time.time()
    cpu_serial(num)
    print(f"{'Serial:':<16} {time.time() - start:.5f}")

    start = time.time()
    cpu_multithreading(cpu_heavy, range(num), num)
    print(f"{'Multithreading:':<16} {time.time() - start:.5f}")

    start = time.time()
    cpu_multiprocessing(cpu_heavy, range(num), num if num <= 4 else 4)
    print(f"{'Multiprocessing:':<16} {time.time() - start:.5f}")


def run_io_bound():
    """Run all IO functions."""
    print("\n--------\nio heavy\n--------")
    session = requests.Session()

    start = time.time()
    io_serial(session)
    print(f"{'Serial:':<16} {time.time() - start:.5f}")

    start = time.time()
    io_multithreading(io_heavy, itertools.repeat(session), range(n_jobs), n_jobs)
    print(f"{'Multithreading:':<16} {time.time() - start:.5f}")

    start = time.time()
    asyncio.run(download_all_sites(urls))
    print(f"{'Asyncio:':<16} {time.time() - start:.5f}")

    start = time.time()
    io_multiprocessing(io_heavy, itertools.repeat(session), range(n_jobs), 4)
    print(f"{'Multiprocessing:':<16} {time.time() - start:.5f}\n")


if __name__ == "__main__":
    urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 100
    n_jobs = len(urls)

    run_cpu_bound()
    run_io_bound()
