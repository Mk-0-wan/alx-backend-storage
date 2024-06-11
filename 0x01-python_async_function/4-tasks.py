#!/usr/bin/env python3

"""Passing synchronous function to return a async object"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


def fix_array(arry: list, elem: float) -> list:
    """Returns a sorted array in an ascending order"""
    if not arry:
        arry.append(elem)
    for idx in range(len(arry)):
        if elem < arry[idx]:
            arry.insert(idx, elem)
    arry.append(elem)
    return arry


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Making mulitiple concurrency co-routine"""
    # make a list of all the co-routines returned
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    await_list = []
    # append to th list all the early task completed in the tasks routine
    for task in asyncio.as_completed(tasks):
        finished = await task
        fix_array(await_list, finished)

    return await_list
