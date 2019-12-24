#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Async experiments. See https://realpython.com/python-concurrency/"""

import asyncio
import time

import aiohttp
import requests
from yaspin import yaspin


def serial_download_site(session, url):
    with session.get(url) as response:
        return response


def serial_download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            serial_download_site(session, url)


def run_serial(sites):
    start_time = time.time()
    serial_download_all_sites(sites)
    duration = time.time() - start_time
    return (len(sites), duration)


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


def run_async(sites):
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    return (len(sites), duration)


if __name__ == "__main__":
    sites = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 20
    with yaspin(text="Running serial", color="green") as spinner:
        serial = run_serial(sites)
        spinner.text = "Serial: %s sites in %s seconds" % serial
        spinner.ok()
    with yaspin(text="Running async", color="green") as spinner:
        unsync = run_async(sites)
        spinner.text = "Async:  %s sites in %s seconds" % unsync
        spinner.ok()
