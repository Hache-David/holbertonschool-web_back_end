#!/usr/bin/env python3
'''measure_runtime should measure
the total runtime and return it.'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''efvqfvqsfvqdf'''
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return (end - start)
