#!/usr/bin/env python3
"""Compare threading, asyncio, and multiprocessing."""

import asyncio
import itertools
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import httpx

urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 20
n_links = len(urls)
n_tasks = 4


def cpu_heavy(x):
    """Perform a CPU heavy task."""
    count = x
    for i in range(10**8):
        count += i
    return x


def cpu_serial(n_tasks):
    """Run serial."""
    result = []
    for x in range(n_tasks):
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
    response = session.get(urls[x])
    return response


def io_heavy_for_multiprocessing(x):
    """Perform an IO heavy task for multiprocessing (creates its own session)."""
    with httpx.Client() as session:
        response = session.get(urls[x])
        return response


def io_serial() -> None:
    """Run serial."""
    with httpx.Client() as session:
        for x in range(n_links):
            io_heavy(session, x)


def io_multithreading(func, session, x, workers):
    """Run multithreaded."""
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, session, x)
    return list(res)


def io_multiprocessing(func, x, workers):
    """Run multiprocessed."""
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, x)
    return list(res)


async def download_site(session, url):
    """Async download."""
    response = await session.get(url)
    return response


async def download_all_sites(sites):
    """Async all downloads."""
    async with httpx.AsyncClient() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        await asyncio.gather(*tasks, return_exceptions=True)
    return tasks


def run_cpu_bound() -> None:
    """Run all CPU functions."""
    print("=" * 50)
    print("CPU-BOUND TASKS COMPARISON")
    print("=" * 50)

    print(f"\n1. Serial execution (n_tasks={n_tasks}):")
    start_time = time.time()
    serial_result = cpu_serial(n_tasks)
    serial_time = time.time() - start_time
    print(f"   Runs: {serial_result}")
    print(f"   Time taken: {serial_time:.4f} seconds")

    print(f"\n2. Multithreading execution (workers={n_tasks}):")
    start_time = time.time()
    threading_result = cpu_multithreading(cpu_heavy, range(n_tasks), n_tasks)
    threading_time = time.time() - start_time
    print(f"   Runs: {threading_result}")
    print(f"   Time taken: {threading_time:.4f} seconds")

    workers = n_tasks if n_tasks <= 4 else 4
    print(f"\n3. Multiprocessing execution (workers={workers}):")
    start_time = time.time()
    multiprocessing_result = cpu_multiprocessing(cpu_heavy, range(n_tasks), workers)
    multiprocessing_time = time.time() - start_time
    print(f"   Runs: {multiprocessing_result}")
    print(f"   Time taken: {multiprocessing_time:.4f} seconds")

    print("\nCPU-BOUND SUMMARY:")
    print(f"   Serial:         {serial_time:.4f}s")
    print(f"   Multithreading: {threading_time:.4f}s")
    print(f"   Multiprocessing: {multiprocessing_time:.4f}s")

    print("\nPerformance improvements vs serial:")
    print(f"   Multithreading: {serial_time / threading_time:.2f}x faster")
    print(f"   Multiprocessing: {serial_time / multiprocessing_time:.2f}x faster")


def run_io_bound() -> None:
    """Run all IO functions."""
    print("\n" + "=" * 50)
    print("IO-BOUND TASKS COMPARISON")
    print("=" * 50)

    print(f"\n1. Serial execution ({n_links} requests):")
    start_time = time.time()
    io_serial()
    serial_time = time.time() - start_time
    print(f"   Completed {n_links} HTTP requests")
    print(f"   Time taken: {serial_time:.4f} seconds")

    print(f"\n2. Multithreading execution (workers={n_links}):")
    start_time = time.time()
    with httpx.Client() as session:
        threading_result = io_multithreading(
            io_heavy, itertools.repeat(session), range(n_links), n_links
        )
    threading_time = time.time() - start_time
    print(f"   Completed {len(threading_result)} HTTP requests")
    print(f"   Time taken: {threading_time:.4f} seconds")

    print(f"\n3. Async execution ({len(urls)} requests):")
    start_time = time.time()
    async_result = asyncio.run(download_all_sites(urls))
    async_time = time.time() - start_time
    print(f"   Completed {len(async_result)} HTTP requests")
    print(f"   Time taken: {async_time:.4f} seconds")

    print("\n4. Multiprocessing execution (workers=4):")
    start_time = time.time()
    multiprocessing_result = io_multiprocessing(io_heavy_for_multiprocessing, range(n_links), 4)
    multiprocessing_time = time.time() - start_time
    print(f"   Completed {len(multiprocessing_result)} HTTP requests")
    print(f"   Time taken: {multiprocessing_time:.4f} seconds")

    print("\nIO-BOUND SUMMARY:")
    print(f"   Serial:         {serial_time:.4f}s")
    print(f"   Multithreading: {threading_time:.4f}s")
    print(f"   Async:          {async_time:.4f}s")
    print(f"   Multiprocessing: {multiprocessing_time:.4f}s")

    print("\nPerformance improvements vs serial:")
    print(f"   Multithreading: {serial_time / threading_time:.2f}x faster")
    print(f"   Async:          {serial_time / async_time:.2f}x faster")
    print(f"   Multiprocessing: {serial_time / multiprocessing_time:.2f}x faster")


if __name__ == "__main__":
    print()
    run_cpu_bound()
    run_io_bound()
    print("\n" + "=" * 70 + "\n")
