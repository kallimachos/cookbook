#!/usr/bin/env python3
"""Async progressbar."""

import asyncio
import time

import aiohttp
from tqdm.asyncio import tqdm


async def download_site(session, url):
    """Async download."""
    return await session.get(url)


async def download_all_sites(sites):
    """Async all downloads."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        return await tqdm.gather(tasks)
        # result = [
        #     await f
        #     for f in tqdm(asyncio.as_completed(tasks), total=len(tasks))
        # ]


if __name__ == "__main__":
    urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 100
    start = time.time()
    result = asyncio.run(download_all_sites(urls))
    for _r in result:
        pass
