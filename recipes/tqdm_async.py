#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Async progressbar."""

import asyncio
import time

import aiohttp
from tqdm.asyncio import tqdm


async def download_site(session, url):
    """Async download."""
    response = await session.get(url)
    return response


async def download_all_sites(sites):
    """Async all downloads."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        result = await tqdm.gather(*tasks)
        # result = [
        #     await f
        #     for f in tqdm(asyncio.as_completed(tasks), total=len(tasks))
        # ]
    return result


if __name__ == "__main__":
    urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 100
    start = time.time()
    result = asyncio.run(download_all_sites(urls))
    for r in result:
        print(f"{r.url}: {r.status}")
