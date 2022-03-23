"""
The user directory is disabled under some circumstances that would pose security issues
(for example, if the process is running with a different effective user or group ID than
the actual user who started it). An application can check the setting by examining ENABLE_
USER_SITE.

The user directory can also be explicitly disabled on the command line with -s.
"""

import site
status = {
    None: 'Disabled for security',
    True: 'Enabled',
    False: 'Disabled by command-line option',
}
print('Flag :', site.ENABLE_USER_SITE)
print('Meaning:', status[site.ENABLE_USER_SITE])