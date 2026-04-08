#!/usr/bin/env python3
"""Module for measuring async function runtime."""

import time
import asyncio
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time per coroutine for wait_n.
    
    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay in seconds
    
    Returns:
        Average execution time per coroutine (total_time / n)
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n
