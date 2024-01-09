#!/usr/bin/env python3
"""
Module defines a task_wait_random function that takes an integer max_delay
argument and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task.
    """
    # Creates a task from the coroutine, then schedules execution.
    return asyncio.create_task(wait_random(max_delay))