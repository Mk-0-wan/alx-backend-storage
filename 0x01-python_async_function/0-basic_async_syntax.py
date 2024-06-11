#!/usr/bin/env python3
"""Making a co-oroutine"""
import asyncio
import random


async def wait_random(max_delay: float = random.uniform(0, 10)) -> float:
    """return a radmom float value"""
    await asyncio.sleep(max_delay)
    return max_delay
