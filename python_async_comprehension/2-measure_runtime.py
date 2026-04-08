#!/usr/bin/env python3
"""Module for measuring concurrent async comprehension runtime.

This module provides functionality to measure the total execution time
of multiple async_comprehension coroutines executed concurrently using
asyncio.gather(). It demonstrates performance analysis of asynchronous
operations and concurrent task execution.
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of executing 4 async_comprehension coroutines.

    Creates 4 async_comprehension coroutines and executes them concurrently
    using asyncio.gather(). Records the total elapsed time from start to
    completion of all concurrent tasks.

    Returns:
        float: The total time in seconds taken to execute all 4
            async_comprehension coroutines concurrently.
    """
    tasks = [async_comprehension() for i in range(4)]

    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
