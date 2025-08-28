#!/usr/bin/env python3
"""Asyncio lock test script."""

import asyncio
import time

import aiohttp

urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 10


async def download_site(session, url, lock):
    """Async download."""
    async with lock:
        print("Lock acquired for", url)
        return await session.get(url)


async def download_all_sites(sites, lock):
    """Async all downloads."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url, lock))
        await asyncio.gather(*tasks, return_exceptions=True)
    return tasks


def run_io_bound() -> None:
    """Run all IO functions."""
    tstart = time.time()
    lock = asyncio.Lock()
    asyncio.run(download_all_sites(urls, lock))
    print(f"{len(urls)} pages fetched in {time.time() - tstart} seconds")


if __name__ == "__main__":
    run_io_bound()
