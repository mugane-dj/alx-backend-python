#!/usr/bin/env python3
"""
async_generator - implements a coroutine that yields a
                  random float number between 0 and 10
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The async_generator function is an asynchronous generator
    that yields random float numbers between 0 and 10, with a
    delay of 1 second between each yield.
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
