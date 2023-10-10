#!/usr/bin/env python3
""" Async Generators and comprehensions """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """ Generates random numbers asynchronously """
    a = 10
    while a > 0:
        yield random.uniform(0, 10)
        a -= 1
        await asyncio.sleep(1)
