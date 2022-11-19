"""
The asyncio event loop can start a coroutine in several different ways. The simplest approach
is to use run_until_complete(), passing the coroutine to this method directly.
"""

import asyncio



async def coroutine():
    print('in coroutine')

event_loop = asyncio.get_event_loop()

try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    event_loop.run_until_complete(coro)
finally:
    print('closing event loop')
    event_loop.close()