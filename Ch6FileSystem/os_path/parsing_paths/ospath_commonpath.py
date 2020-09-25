"""
commonpath() does honor path separators. It returns a prefix that does not include partial
path values.
"""

import os.path

paths = ['/one/two/three/four',
        '/one/two/threefold',
        '/one/two/three/',
]

for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonpath(paths))

"""
Because "threefold" does not have a path separator after "three", the common prefix is
/one/two.
"""