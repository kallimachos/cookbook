#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example using semaphores with aiofiles."""

import asyncio
from pathlib import Path

import aiofiles


async def write_to_disk(fname, sema):
    """Async write."""
    filepath = Path("files", fname)
    async with sema:
        async with aiofiles.open(filepath, "w+") as f:
            print("Writing", filepath)
            await f.write("asdf")
            print("Done writing", filepath)


async def read_file(fname, sema):
    """Async read."""
    filepath = Path("files", fname)
    async with sema:
        async with aiofiles.open(filepath, "r") as f:
            print("Reading", filepath)
            text = await f.read()
            print("Done reading", filepath)
    return text


async def tasks():
    """Run tasks."""
    sema = asyncio.Semaphore(100)  # Allow 100 concurrent writers
    # tasks = [asyncio.create_task(write_to_disk(f"{i}.txt", sema)) for i in range(10000)]
    tasks = [asyncio.create_task(read_file(f"{i}.txt", sema)) for i in range(10000)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(tasks())
