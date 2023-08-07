"""
wait_n - An async routine that spans wait_random for n times
then returns the list of delays sorted in ascending order.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    The `wait_n` function takes in two parameters, `n` and `max_delay`,
    and returns a list of `n` random delays.

    :param n: The parameter `n` is an integer that represents
              the number of times the `wait_random` function
              should be called and awaited
    :type n: int
    :param max_delay: The `max_delay` parameter represents
                      the maximum amount of time (in seconds) that
                      each `wait_random` function call can take
    :type max_delay: int
    :return: The function `wait_n` returns a list of floats, which
             represents the delays obtained from calling the
             `wait_random` function `n` times.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
