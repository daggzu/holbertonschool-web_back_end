#!/usr/bin/env python3
"""
Module defines a basic async function that waits for a random delay
between 0 and max_delay(limited wait time) seconds and eventually
returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and
    eventually returns it.
    """
    delay = random.uniform(0, max_delay)  # Random delay
    await asyncio.sleep(delay)  # Wait for the random delay
    return delay