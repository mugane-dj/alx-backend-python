#!/usr/bin/env python3
"""
task_wait_n - modifies wait_n by calling task_wait_random
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The function `task_wait_n` takes in two parameters, `n` and
    `max_delay`, and returns a sorted list of `n` random delays.

    :param n: The parameter `n` represents the number of tasks
              to be executed
    :type n: int
    :param max_delay: The `max_delay` parameter represents the
                      maximum amount of time (in seconds) that
                      each task can wait before completing
    :type max_delay: int
    :return: The function `task_wait_n` returns a sorted list
             of floats, which represents the delays obtained
             from calling the `task_wait_random` function `n` times.
    """
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
