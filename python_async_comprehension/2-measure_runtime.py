#!/usr/bin/env python3
'''measure_runtime should measure
the total runtime and return it.'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension four times in parallel and
    measures total runtime.'''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    return (end - start)
