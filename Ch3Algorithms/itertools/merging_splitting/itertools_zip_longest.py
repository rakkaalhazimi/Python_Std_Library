"""
zip() stops when the first input iterator is exhausted. To process all of the inputs, even if
the iterators produce different numbers of values, use zip_longest().
"""

from itertools import zip_longest

r1 = range(3)
r2 = range(2)

print('zip stops early:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')
print(list(zip_longest(r1, r2)))

"""
By default, zip_longest() substitutes None for any missing values. Use the fillvalue
argument to use a different substitute value.
"""