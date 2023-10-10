#!/usr/bin/env python3
""" Async Generators and comprehensions """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async comprehension """
    return [_ async for _ in async_generator()]
