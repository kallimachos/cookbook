#!/usr/bin/env python3
"""Compare httpx and aiohttp."""

import asyncio
import time

import aiohttp
import httpx
import requests

count = 10
geturl = "https://www.jython.org"
posturl = "https://httpbin.org/post"
data = {"key": "value"}


with requests.Session() as client:
    start_time = time.perf_counter()
    for _ in range(count):
        client.get(geturl)
    end_time = time.perf_counter()


with httpx.Client(follow_redirects=True) as client:
    start_time = time.perf_counter()
    for _ in range(count):
        client.get(geturl)
    end_time = time.perf_counter()


with httpx.Client(http2=True, follow_redirects=True) as client:
    start_time = time.perf_counter()
    for _ in range(count):
        client.get(geturl)
    end_time = time.perf_counter()




async def get() -> None:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        time.perf_counter()
        tasks = [client.get(geturl) for _ in range(count)]
        await asyncio.gather(*tasks)
        time.perf_counter()

    async with httpx.AsyncClient(http2=True, follow_redirects=True) as client:
        time.perf_counter()
        tasks = [client.get(geturl) for _ in range(count)]
        await asyncio.gather(*tasks)
        time.perf_counter()

    async with aiohttp.ClientSession() as client:
        time.perf_counter()
        tasks = [client.get(geturl) for _ in range(count)]
        await asyncio.gather(*tasks)
        time.perf_counter()


asyncio.run(get())



async def post() -> None:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        time.perf_counter()
        tasks = [client.post(posturl, data=data) for _ in range(count)]
        await asyncio.gather(*tasks)
        time.perf_counter()

    async with httpx.AsyncClient(http2=True, follow_redirects=True) as client:
        time.perf_counter()
        tasks = [client.post(posturl, data=data) for _ in range(count)]
        await asyncio.gather(*tasks)
        time.perf_counter()

    async with aiohttp.ClientSession() as client:
        time.perf_counter()
        tasks = [client.post(posturl, data=data) for _ in range(count)]
        await asyncio.gather(*tasks)
        time.perf_counter()


asyncio.run(post())
