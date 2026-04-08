#!/usr/bin/env python3
"""Module that implements an asynchronous generator for random numbers.

This module demonstrates the use of async generators in Python, providing
a coroutine that yields random floating-point numbers at regular intervals
using asyncio for asynchronous delays between yields.
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Asynchronously generate random numbers with delays between yields.

    This async generator coroutine yields ten random floating-point numbers
    between 0 and 10, pausing for one second between each yield to simulate
    an asynchronous operation and demonstrate concurrent execution patterns.

    Yields:
        float: A random number between 0 and 10 for each of the 10 iterations.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        