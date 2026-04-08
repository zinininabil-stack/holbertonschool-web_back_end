#!/usr/bin/env python3
"""Module for spawning multiple tasks using task_wait_random."""

import asyncio
from typing import List

# Import task_wait_random from the previous task module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn task_wait_random n times and return the list of delays.

    The implementation mirrors wait_n, but uses task_wait_random to
    create asyncio.Task objects instead of calling wait_random directly.
    The list of delays is built in the order tasks complete, which
    corresponds to ascending delay times without calling sort().
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = []

    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
