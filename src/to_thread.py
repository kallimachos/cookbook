import asyncio
import time


async def test():
    tasks = []
    for _item in range(10):
        tasks.append(asyncio.to_thread(time.sleep, 1))
    return await asyncio.gather(*tasks)


asyncio.run(test())
