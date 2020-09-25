"""
commonprefix() takes a list of paths as an argument and returns a single string that
represents a common prefix present in all of the paths. The value may represent a path that
does not actually exist, and the path separator is not included in the consideration. As a
consequence, the prefix might not stop on a separator boundary.
"""

import os.path

paths = ["one/two/three/four",
         "one/two/threefold",
         "one/two/three/",
         ]
for path in paths:
    print("PATH:", path)

print()
print("PREFIX:", os.path.commonprefix(paths))

"""
In this example, the common prefix string is /one/two/three, even though one path does
not include a directory named three.
"""