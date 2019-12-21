#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare threading, asyncio, and multiprocessing."""

import aiohttp
import asyncio
import itertools
import requests
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def multithreading(func, session, x, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, session, x)
    return list(res)


def multiprocessing(func, session, x, workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, session, x)
    return list(res)


def cpu_heavy(session, x):
    count = x
    for i in range(10**8):
        count += i
    return x


def io_heavy(session, x):
    with session.get(urls[x]) as response:
        return response


async def download_site(session, url):
    async with session.get(url) as response:
        return response


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
    return tasks


def run_cpu_bound():
    print("\n---------\ncpu heavy\n---------")
    num = 2

    start = time.time()
    result = []
    for x in range(num):
        result.append(cpu_heavy(range(num), x))
    print(f"Serial: {time.time() - start}")

    start = time.time()
    result = multithreading(cpu_heavy, range(num), range(num), 4)
    print(f"Multithreading: {time.time() - start}")

    start = time.time()
    result = multiprocessing(cpu_heavy, range(num), range(num), 4)
    print(f"Multiprocessing: {time.time() - start}")


def run_io_bound():
    print("\n--------\nio heavy\n--------")
    session = requests.Session()

    start = time.time()
    for x in range(n_jobs):
        io_heavy(session, x)
    print(f"Serial: {time.time() - start}")

    start = time.time()
    multithreading(io_heavy, itertools.repeat(session), range(n_jobs), n_jobs)
    print(f"Multithreading: {time.time() - start}")

    start = time.time()
    asyncio.run(download_all_sites(urls))
    print(f"Asyncio: {time.time() - start}")

    start = time.time()
    multiprocessing(io_heavy, itertools.repeat(session), range(n_jobs), 4)
    print(f"Multiprocessing: {time.time() - start}")


if __name__ == "__main__":
    urls = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    n_jobs = len(urls)

    # run_cpu_bound()
    run_io_bound()
