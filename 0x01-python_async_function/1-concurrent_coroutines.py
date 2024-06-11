#!/usr/bin/env python3
"""Making multiple co-routine objects"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Making mulitiple concurrency co-routine"""
    await_list = []
    for _ in range(n):
        await_list.append(await wait_random(max_delay))
    return await_list
