#!/usr/bin/env python3
"""Making a co-oroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """return a radmom float value"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return max_delay
