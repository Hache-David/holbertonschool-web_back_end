#!/usr/bin/env python3
'''The coroutine will loop 10 times'''

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[None, None]:
    '''jzzhbzjhb'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
