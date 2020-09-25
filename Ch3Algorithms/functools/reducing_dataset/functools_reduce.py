"""
The reduce() function takes a callable and a sequence of data as input. It produces a
single value as output based on invoking the callable with the values from the sequence and
accumulating the resulting output.
"""

import functools

def do_reduce(a, b):
    print('do_reduce({}, {})'.format(a, b))
    return a + b

data = range(1, 5)
print(data)
result = functools.reduce(do_reduce, data) # It has initializer argument
print('result: {}'.format(result))