#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Async experiments. See https://learning.oreilly.com/library/view/hands-on-reactive-programming/9781789138726/fee472d4-d7f5-4ea6-aa5b-78a3a0250366.xhtml"""

import aiohttp
import asyncio
import time


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


start_time = time.time()
sites = ["http://www.jython.org",
         "http://olympus.realpython.org/dice",
         ] * 5
result = asyncio.run(download_all_sites(sites))
duration = time.time() - start_time
print("%s sites in %s seconds" % (len(sites), duration))
