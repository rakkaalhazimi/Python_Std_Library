"""
Besides taking existing paths apart, it is frequently necessary to build paths from other
strings. To combine several path components into a single value, use join().
"""

import os.path

PATHS = [
    ("one", "two", "three"),
    ("/", "one", "two", "three"),
    ("/one", "/two", "/three"),
]

for parts in PATHS:
    print("{} : {!r}".format(parts, os.path.join(*parts)))

"""
If any argument to join begins with os.sep, all of the previous arguments are discarded and
the new one becomes the beginning of the return value.
"""