#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Async experiments."""

import aiohttp
import asyncio
import time


async def get(session, url):
    async with session.get(url) as response:
        return(await response.text())


async def download_all_sites(sites):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in sites:
            task = asyncio.ensure_future(get(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
    print(tasks[0].result())


if __name__ == "__main__":
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 5
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print("Async: %s sites in %s seconds" % (len(sites), duration))
