"""
The repeat() function returns an iterator that produces the same value each time it is
accessed.
"""

from itertools import repeat

for i in repeat('over-and-over', 5):
    print(i)