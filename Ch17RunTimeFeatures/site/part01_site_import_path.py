"""
site is automatically imported each time the interpreter starts up. As it is being imported,
it extends sys.path with site-specific names that are constructed by combining the prefix
values sys.prefix and sys.exec_prefix with several suffixes. The prefix values used are
saved in the module-level variable PREFIXES for later reference.
"""

import sys
import os
import site

if 'Windows' in sys.platform:
    SUFFIXES = [
        '',
        'lib/site-packages',
    ]
else:
    SUFFIXES = [
        'lib/python{}/site-packages'.format(sys.version[:3]),
        'lib/site-python',
    ]

print('Path prefixes:')
for p in site.PREFIXES:
    print(' ', p)

for prefix in sorted(set(site.PREFIXES)):
    print()
    print(prefix)

    for suffix in SUFFIXES:
        print()
        print(' ', suffix)
        path = os.path.join(prefix, suffix).rstrip(os.sep)
        print(' exists :', os.path.exists(path))
        print(' in path:', path in sys.path)