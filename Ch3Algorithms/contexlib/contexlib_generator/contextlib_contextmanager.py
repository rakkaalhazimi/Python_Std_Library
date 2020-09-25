

import contextlib

@contextlib.contextmanager
def make_context():
    print(' entering')
    try:
        # The value yielded, if any, is bound to the variable in the as clause of the with
        # statement.
        yield {}
    except RuntimeError as err:
        print(' ERROR:', err)
    finally:
        print(' exiting')

print('Normal:')
with make_context() as value:
    print(' inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')

# Exceptions from within the with block are raised again inside the generator, so
# they can be handled there.