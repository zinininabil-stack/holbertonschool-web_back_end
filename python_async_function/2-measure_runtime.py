#!/usr/bin/env python3
"""Module for measuring the execution time of async operations.

This module provides a function that measures how long it takes to execute
concurrent coroutines and returns the average execution time.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time to execute n wait_random coroutines.

    This function runs n concurrent coroutines with the specified maximum
    delay and calculates the average time taken per coroutine.

    Args:
        n: The number of concurrent coroutines to execute.
        max_delay: The maximum delay in seconds for each coroutine.

    Returns:
        The average execution time per coroutine in seconds.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
