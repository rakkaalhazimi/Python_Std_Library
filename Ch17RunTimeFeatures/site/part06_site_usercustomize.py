"""
Similar to sitecustomize, the usercustomize module can be used to establish user-specific
settings each time the interpreter starts up. usercustomize is loaded after sitecustomize,
so site-wide customizations can be overridden.

In environments where a user’s home directory is shared on several servers running
different operating systems or versions, the standard user directory mechanism may not
work for user-specific installations of packages. In these cases, a platform-specific directory
tree can be used instead.

run: set PYTHONPATH=with_usercustomize && python part06_site_usercustomize.py
"""

import sys
print('Running main program from\n{}'.format(sys.argv[0]))
print('End of path:', sys.path[-1])