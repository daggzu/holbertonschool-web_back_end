#!/usr/bin/env python3
"""
Module defines a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    total_time = time.perf_counter() - start_time
    return total_time