print('Loading usercustomize.py')

import site
import platform
import os
import sys

path = os.path.expanduser(os.path.join('~',
    'python',
    sys.version[:3],
    platform.platform(),
))
print('Adding new path', path)
site.addsitedir(path)