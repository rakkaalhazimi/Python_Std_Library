"""
The try:except form can be replaced with contextlib.suppress() to more explicitly
suppress a class of exceptions happening anywhere within the with block.
"""

import contextlib

class NonFatalError(Exception):
    pass

def non_idempotent_operation():
    raise NonFatalError(
        'The operation failed because of existing state'
    )

with contextlib.suppress(ValueError):
    print('trying non-idempotent operation')
    # non_idempotent_operation()
    raise ValueError("Remember madafaka ?")
    print('succeeded!')

print('done')