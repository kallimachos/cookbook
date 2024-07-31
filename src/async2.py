#!/usr/bin/env python3
"""Asyncio test script."""

import asyncio
import time

import aiohttp

urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 100


async def download_site(session, url):
    """Async download."""
    return await session.get(url)


async def download_all_sites(sites):
    """Async all downloads."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        await asyncio.gather(*tasks, return_exceptions=True)
    return tasks


def run_io_bound() -> None:
    """Run all IO functions."""
    tstart = time.time()
    asyncio.run(download_all_sites(urls))
    print(f"{len(urls)} pages fetched in {time.time() - tstart} seconds")


if __name__ == "__main__":
    run_io_bound()
