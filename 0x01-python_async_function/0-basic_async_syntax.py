#!/usr/bin/env python3
""" Async function """

import asyncio as asyn
import random


async def wait_random(max_delay: int=10) -> float:
    """ Await random async function """
    sleeptime = random.uniform(0, max_delay)
    await asyn.sleep(sleeptime)
    return sleeptime