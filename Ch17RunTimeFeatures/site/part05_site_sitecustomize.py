"""
The site module is responsible for loading site-wide customization defined by the local site
owner in a sitecustomize module. Uses for sitecustomize include extending the import
path and enabling coverage, profiling, or other development tools.

For example, the sitecustomize.py script in the following listing extends the import
path with a directory based on the current platform. The platform-specific 
path in /opt/python is added to the import path, so any packages installed there can be imported.

This kind of system is useful for sharing packages containing compiled extension modules
between hosts on a network via a shared file system. Only the sitecustomize.py script
needs to be installed on each host; the other packages can be accessed from the file server.

run: set PYTHONPATH=with_sitecustomize && python part05_site_sitecustomize.py

Since sitecustomize is meant for system-wide configuration, it should be installed
somewhere in the default path (usually in the site-packages directory). This example sets
PYTHONPATH explicitly to ensure the module is picked up.
"""

import sys
print('Running main program from\n{}'.format(sys.argv[0]))
print('End of path:', sys.path[-1])