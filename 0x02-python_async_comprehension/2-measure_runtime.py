#!/usr/bin/env python3

"""Making parallel asychronous calls"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runs parallel coroutines"""
    start: float = time.perf_counter()
    _ = await asyncio.gather(
             async_comprehension(),
             async_comprehension(),
             async_comprehension(),
             async_comprehension(),)
    end: float = time.perf_counter()
    return (end - start)