#!/usr/bin/env python3
"""Experiment with adding tasks to a running loop."""

import asyncio
import time

import aiohttp


async def download_site(session, url) -> None:
    """Async download."""
    await session.get(url)
    loop = asyncio.get_event_loop()
    nrls = ["http://www.google.com", "http://example.com"] * 2
    tasks = []
    for nrl in nrls:
        task = loop.create_task(session.get(nrl))
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for _result in results:
        pass


async def download_all_sites(sites):
    """Async all downloads."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        await asyncio.gather(*tasks, return_exceptions=True)
    return tasks


if __name__ == "__main__":
    urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"]
    start = time.time()
    result = asyncio.run(download_all_sites(urls))
