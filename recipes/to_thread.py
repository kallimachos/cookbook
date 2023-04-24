import asyncio
import time


async def test():
    tasks = []
    for item in range(10):
        print(item)
        tasks.append(asyncio.to_thread(time.sleep, 1))
    result = await asyncio.gather(*tasks)
    return result

asyncio.run(test())
