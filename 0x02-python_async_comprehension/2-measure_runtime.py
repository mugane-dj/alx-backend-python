#!/usr/bin/env python3
"""
worker - implements a function `worker` that calls
         the async_comprehension function
measure_runtime - implements a function `measure_runtime`
                  that measures the total runtime of executing the `worker`
                  function asynchronously for `n` times.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def worker() -> None:
    """
    The `worker` function is an asynchronous function that
    calls the `async_comprehension` function.
    """
    await async_comprehension()


async def measure_runtime() -> float:
    """
    The `measure_runtime` function measures the total runtime
    of executing the `worker` function
    asynchronously for `n` times.
    :return: The function `measure_runtime` returns a float value
             representing the total runtime of the asynchronous tasks.
    """
    n = 4
    tasks = []
    start_time = time.time()
    for _ in range(n):
        task = asyncio.create_task(worker())
        tasks.append(task)

    await asyncio.gather(*tasks)
    stop_time = time.time()
    total_runtime = stop_time - start_time
    return total_runtime


asyncio.run(measure_runtime())
