#!/usr/bin/env python3
"""
Module defines a measure_time function that measures the total execution time
for wait_n(n, max_delay), and returns the total time as float.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the total execution time for wait_n(n, max_delay), and returns the
    total time as float.
    """
    start = time.perf_counter()  # Start time of coroutine
    asyncio.run(wait_n(n, max_delay))  # Run coroutine
    end = time.perf_counter()  # End time of coroutine
    return (end - start) / n