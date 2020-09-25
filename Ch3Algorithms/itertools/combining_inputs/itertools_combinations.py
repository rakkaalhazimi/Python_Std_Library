"""
To limit the values to unique combinations rather than permutations, use
combinations(). As long as the members of the input are unique, the output will not
include any repeated values.
"""

from itertools import *

def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()

print('Unique pairs:\n')
show(combinations('abcd', r=2))