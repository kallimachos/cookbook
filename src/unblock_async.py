#!/usr/bin/env python3
"""Experiment with making sync calls in the event loop unblocking."""

import asyncio
import time

import aiohttp
import requests


async def download_site(loop, session, rsession, url):
    """Async download."""
    aresponse = await session.get(url)
    rresponse = await loop.run_in_executor(None, rsession.get, url)
    return [aresponse, rresponse]


async def download_all_sites(sites):
    """Async all downloads."""
    loop = asyncio.get_event_loop()
    rsession = requests.Session()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(loop, session, rsession, url))
        return await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 100
    start = time.time()
    result = asyncio.run(download_all_sites(urls))
    for _r in result:
        pass
