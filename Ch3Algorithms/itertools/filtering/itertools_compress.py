"""
compress() offers another way to filter the contents of an iterable. Instead of calling a
function, it uses the values in another iterable to indicate when to accept a value and when
to ignore it.
"""

from itertools import compress, cycle

every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()