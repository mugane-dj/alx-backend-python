#!/usr/bin/env python3
"""
wait_random - An asynchronous coroutine that takes in an integer argument
max_delay that waits for a random delay between 0 and max_delay seconds
and eventually returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

asyncio.run(wait_random())
