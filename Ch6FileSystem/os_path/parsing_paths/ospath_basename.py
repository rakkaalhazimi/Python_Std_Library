"""
The basename() function returns a value equivalent to the second part of the split()
value.
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
    print("{!r:>17} : {!r}".format(path, os.path.basename(path)))

"""
The full path is stripped down to the last element, whether that refers to a file or a directory.
If the path ends in the directory separator (os.sep), the base portion is considered to be
empty.
"""