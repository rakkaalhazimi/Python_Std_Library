"""
The split() function breaks the path into two separate parts and returns a tuple with
the results. The second element of the tuple is the last component of the path, and the first
element is everything that comes before it.
"""

import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

for path in PATHS:
    print("{!r:>17} : {!r}".format(path, os.path.split(path)))