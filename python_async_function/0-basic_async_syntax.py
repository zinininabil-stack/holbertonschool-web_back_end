#!/usr/bin/env python3
"""Module for basic async coroutine."""

import asyncio
import random

max_delay: int


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
