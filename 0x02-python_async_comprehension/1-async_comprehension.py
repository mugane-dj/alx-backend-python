#!/usr/bin/env python3
"""
async_comprehension - implements a coroutine that uses an async
                      generator to return 10 random float numbers
                      using async comprehensing
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The function `async_comprehension` returns a list of floats
    obtained from an asynchronous generator.
    :return: The function `async_comprehension` is returning
             a list of floats.
    """
    return [i async for i in async_generator()]
