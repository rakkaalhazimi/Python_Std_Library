"""
The dropwhile() function returns an iterator that produces elements of the input iterator
after a condition becomes false for the first time.
"""

from itertools import dropwhile

def should_drop(x):
    print('Testing:', x)
    return x < 1

for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)