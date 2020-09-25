"""
The starmap() function is similar to map(), but instead of constructing a tuple from
multiple iterators, it splits up the items in a single iterator as arguments to the mapping
function using the * syntax.
"""

from itertools import starmap

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in starmap(lambda x, y: (x, y, x * y), values):
    print('{} * {} = {}'.format(*i))