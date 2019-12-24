#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Async experiments. See https://learning.oreilly.com/library/view/advanced-python-programming/9781838551216/d3b8aec7-6758-415d-a20c-875eb778600e.xhtml"""

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

import requests

executor = ThreadPoolExecutor(max_workers=8)


async def fetch_urls(urls):
    return asyncio.gather(*[loop.run_in_executor(executor, requests.get, url) for url in urls])


start_time = time.time()
loop = asyncio.get_event_loop()
sites = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 5
result = loop.run_until_complete(fetch_urls(sites))
duration = time.time() - start_time
print("%s sites in %s seconds" % (result, duration))
