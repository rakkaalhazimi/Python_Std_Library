"""
The chain() function takes several iterators as arguments and returns a single iterator that
produces the contents of all of the inputs as though they came from a single iterator.
"""

from itertools import chain

for item in chain(["A", "B", "C"], [1, 2, 3]):
    print(item)