"""
The cycle() function returns an iterator that repeats the contents of the arguments it
is given indefinitely.
"""

from itertools import cycle

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)
