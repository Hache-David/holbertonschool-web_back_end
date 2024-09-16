#!/usr/bin/env python3
'''wait_n that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay'''

from typing import List

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''erfververververververv'''
    list_return = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        random = await task
        list_return.append(random)
    return list_return
