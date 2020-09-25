"""
The built-in map() function returns an iterator that calls a function on the values in the
input iterators, and returns the results. It stops when any input iterator is exhausted.
"""

for i in map(lambda x, y: x + y, [1, 2, 3], [3, 4, 5]):
    print(i)