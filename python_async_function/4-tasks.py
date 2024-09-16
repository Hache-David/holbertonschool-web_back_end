#!/usr/bin/env python3
'''Take the code from wait_n and alter
it into a new function task_wait_n'''

from typing import List

import asyncio
import random

wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''erfververververververv'''
    list_return = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        random = await task
        list_return.append(random)
    return list_return
