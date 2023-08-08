#!/usr/bin/env python3
"""
measure_runtime - implements a function `measure_runtime`
                  that measures the total runtime of executing the `worker`
                  function asynchronously for `n` times.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    The `measure_runtime` function measures the total runtime
    of executing the `worker` function asynchronously for `n` times.
    :return: The function `measure_runtime` returns a float value
             representing the total runtime of the asynchronous tasks.
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    stop_time = asyncio.get_running_loop().time()
    total_runtime = stop_time - start_time
    return total_runtime

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(measure_runtime())
