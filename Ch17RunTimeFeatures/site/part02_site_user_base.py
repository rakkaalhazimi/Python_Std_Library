"""
In addition to the global site-packages paths, site is responsible for adding the user-specific
locations to the import path. The user-specific paths are all based on the USER_BASE directory, which is usually located in a part of the file system owned (and writable) by the
current user. Inside the USER_BASE directory is a site-packages directory, with the path
being accessible as USER_SITE.
"""

import site

print('Base:', site.USER_BASE)
print('Site:', site.USER_SITE)