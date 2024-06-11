#!/usr/bin/env python3

"""Making an asynchronous generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """generates random float numbers"""
    for elem in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
