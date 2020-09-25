"""
The dirname() function returns the first part of the split path.
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
    print("{!r:>17} : {!r}".format(path, os.path.dirname(path)))

"""
Combining the results of basename() with dirname() gives the original path.
"""