"""
It is also possible to work with paths that include “variable” components that can be
expanded automatically. For example, expanduser() converts the tilde (~) character to the
name of a user’s home directory.
"""

import os.path

for user in ["", "rakka", "nosuchuser"]:
    lookup = "~" + user
    print("{!r:>15} : {!r}".format(
        lookup, os.path.expanduser(lookup)
    ))

"""
If the user’s home directory cannot be found, the string is returned unchanged, as with
~nosuchuser in this example.
"""