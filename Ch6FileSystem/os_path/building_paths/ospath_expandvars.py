"""
expandvars() is more general, and expands any shell environment variables present in
the path.
"""

import os.path
import os

os.environ["MYVAR"] = "VALUE"

print(os.path.expandvars("/path/to/$MYVAR"))

"""
No validation is performed to ensure that the variable value results in the name of a file
that already exists.
"""