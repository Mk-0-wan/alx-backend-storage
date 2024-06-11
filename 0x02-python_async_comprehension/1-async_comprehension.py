#!/usr/bin/env python3

"""Making an asynchronous generator"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects all the ten random numbers from asyc_gen func"""
    result = [nums async for nums in async_generator()]
    return result
