#!/usr/bin/env python3
"""
measure_time - measures total execution time for wait_n(n, max_delay)
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    The function `measure_time` measures the average execution time
    of the `wait_n` function for a given number of iterations and
    maximum delay.

    :param n: The parameter `n` represents the number of tasks to be executed
    :type n: int
    :param max_delay: The `max_delay` parameter represents the maximum
                      delay in seconds that each task in the `wait_n`
                      function can have
    :type max_delay: int
    :return: The function `measure_time` returns the average execution
             time per task.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    execution_time = stop_time - start_time
    return execution_time / n
