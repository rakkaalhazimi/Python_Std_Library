"""
Paths assembled from separate strings using join() or with embedded variables might end
up with extra separators or relative path components. Use normpath() to clean them up.
"""

import os.path

PATHS = [
    "one//two//three",
    "one/./two/./three",
    "one/../alt/two/three"
]

for path in PATHS:
    print("{!r:>22} : {!r}".format(path, os.path.normpath(path)))

"""
Path segments made up of os.curdir and os.pardir are evaluated and collapsed.
"""

