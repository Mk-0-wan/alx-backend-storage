#!/usr/bin/env python3
"""Measure time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for
    wait_n(n, max_delay) and returns total_time / n."""
    start_time = time.perf_counter()  # Start measuring time
    await wait_n(n, max_delay)  # Await the wait_n coroutine
    end_time = time.perf_counter()  # End measuring time
    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n
