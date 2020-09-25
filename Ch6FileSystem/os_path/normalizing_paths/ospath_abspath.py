"""
To convert a relative path to an absolute filename, use abspath().
"""

import os
import os.path

# os.chdir("/usr")

PATHS = [
    ".",
    "..",
    "./one/two/three",
    "../one/two/three",
]

for path in PATHS:
    print("{!r:>21} : {!r}".format(path, os.path.abspath(path)))

"""
The result is a complete path, starting at the top of the file system tree.
"""