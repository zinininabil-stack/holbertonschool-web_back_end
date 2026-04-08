import asyncio
import random

max_delay: int


async def wait_random(max_delay: int = 10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
