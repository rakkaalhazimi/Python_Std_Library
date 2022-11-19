"""
The return value of a coroutine is passed back to the code that starts and waits for it.
"""

import asyncio



async def coroutine():
    print('in coroutine')
    return 'result'


event_loop = asyncio.get_event_loop()

try:
    return_value = event_loop.run_until_complete(
        coroutine()
    )
    print('it returned: {!r}'.format(return_value))

finally:
    event_loop.close()