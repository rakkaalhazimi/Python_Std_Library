"""
The opposite of dropwhile() is takewhile(). It returns an iterator that itself returns
items from the input iterator as long as the test function returns true.
"""

from itertools import takewhile

def should_take(x):
    print('Testing:', x)
    return x < 2

for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)