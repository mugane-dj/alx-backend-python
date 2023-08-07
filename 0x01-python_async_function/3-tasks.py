"""
task_wait_random - returns a Task object for an async function.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    The function `task_wait_random` creates and returns an asyncio task
    that waits for a random amount of time.

    :param max_delay: The `max_delay` parameter is an integer that
                      represents the maximum delay in
    seconds for the `wait_random` function
    :type max_delay: int
    :return: The function `task_wait_random` returns an `asyncio.Task`
             object.
    """
    return asyncio.create_task(wait_random(max_delay))
