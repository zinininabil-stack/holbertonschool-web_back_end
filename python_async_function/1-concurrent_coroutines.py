#!/usr/bin/env python3
"""Module for concurrent coroutines."""

import asyncio
import importlib
from typing import List

basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random

max_delay: int
n: int


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times and return list of delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
