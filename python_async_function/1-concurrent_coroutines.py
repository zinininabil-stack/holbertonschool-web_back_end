#!/usr/bin/env python3
"""Module for concurrent coroutines."""

import asyncio
import random
import importlib

basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random

max_delay: int
n: int


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """Spawn wait_random n times and return sorted list of delays."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)
    return results
