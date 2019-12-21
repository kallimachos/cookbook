#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Async experiments. See https://learning.oreilly.com/library/view/mastering-concurrency-in/9781789343052/c17de7a7-6856-45a0-ad0e-975f2af73860.xhtml"""


import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def s_countdown(start, name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        time.sleep(delay)
        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))
        n -= 1


def run_serial():
    start = time.perf_counter()
    s_countdown(start, 'A', 1)
    s_countdown(start, 'B', 0.8)
    s_countdown(start, 'C', 0.5)
    print('-' * 40)
    print('Done.')


async def a_countdown(start, name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        await asyncio.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -= 1


def run_async():
    # loop = asyncio.get_event_loop()
    start = time.perf_counter()
    tasks = [
        a_countdown(start, 'A', 1),
        a_countdown(start, 'B', 0.8),
        a_countdown(start, 'C', 0.5)
    ]

    asyncio.run(asyncio.wait(tasks))

    print('-' * 40)
    print('Done.')


async def run_esync():
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(max_workers=3)
    futures = [loop.run_in_executor(
        executor,
        s_countdown,
        *args
        ) for args in [(start, 'A', 1), (start, 'B', 0.8), (start, 'C', 0.5)]]
    await asyncio.gather(*futures)

    print('-' * 40)
    print('Done.')


if __name__ == '__main__':
    run_serial()
    run_async()
    asyncio.run(run_esync())