"""
The result set shown previously includes a repeated value, 77. The bisect module provides
two ways to handle repeats: New values can be inserted either to the left of existing values,
or to the right.

The insort() function is actually an alias for insort_right(), which inserts
an item after the existing value. The corresponding function insort_left() inserts an item
before the existing value.
"""

import bisect
# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New Pos Contents')
print('--- --- --------')

# Use bisect_left and insort_left.
l = []
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}'.format(i, position), l)