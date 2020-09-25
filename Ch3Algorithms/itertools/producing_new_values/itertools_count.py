"""
The count() function returns an iterator that produces consecutive integers, indefinitely.
The first number can be passed as an argument (the default is zero).
"""

from itertools import count

# Count() has start, step arguments
for i in zip(count(1), ['a', 'b', 'c']):
    print(i)