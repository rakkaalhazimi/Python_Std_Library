"""
An ExitStack instance maintains a stack data structure of cleanup callbacks. The callbacks
are populated explicitly within the context, and any registered callbacks are called
in the reverse order when control flow exits the context. The result is similar to having
multiple nested with statements, except they are established dynamically.
"""

import contextlib

@contextlib.contextmanager
def make_context(i):
    print('{} entering'.format(i))
    yield {}
    print('{} exiting'.format(i))

def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)

variable_stack(3, 'inside context')