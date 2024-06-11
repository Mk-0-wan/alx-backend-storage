#!/usr/bin/env python3
"""Synchronous function returning an asynchronous object"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an asyncio.Task object"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
