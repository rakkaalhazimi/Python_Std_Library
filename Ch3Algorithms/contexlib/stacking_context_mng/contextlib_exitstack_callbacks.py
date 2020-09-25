"""
ExitStack also supports arbitrary callbacks for closing a context, making it easy to clean
up resources that are not controlled via a context manager.
"""

import contextlib

def callback(*args, **kwds):
    print('closing callback({}, {})'.format(args, kwds))

with contextlib.ExitStack() as stack:
    stack.callback(callback, 'arg1', 'arg2')
    stack.callback(callback, arg3='val3')