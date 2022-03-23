"""
As paths are added to the import path, they are also scanned for path configuration files. A
path configuration file is a plain text file with the extension .pth. Each line in the file can
take one of four forms:

• A full or relative path to another location that should be added to the import path.
• A Python statement to be executed. All such lines must begin with an import statement.
• A blank line that is ignored.
• A line starting with # that is treated as a comment and ignored.

Path configuration files can be used to extend the import path to look in locations that
would not have been added automatically. For example, the setuptools package adds a
path to easy-install.pth when it installs a package in development mode using python
setup.py develop.

The function for extending sys.path is public, and it can be used in example programs
to show how the path configuration files work. Suppose a directory named with_modules
contains the file mymodule.py, with the following print statement showing how the module
was imported.

This script shows how addsitedir() extends the import path so the interpreter can find
the desired module.

run: python part04_site_addsitedir.py with_modules

------------------------------------------------------------------------------------------------
If the directory given to addsitedir() includes any files matching the pattern
*.pth, they are loaded as path configuration files.

run: python part04_site_addsitedir.py with_pth


"""

import site
import os
import sys

script_directory = os.path.dirname(__file__)
module_directory = os.path.join(script_directory, sys.argv[1])
try:
    import mymodule
except ImportError as err:
    print('Could not import mymodule:', err)

print()
before_len = len(sys.path)
site.addsitedir(module_directory)
print('New paths:')
for p in sys.path[before_len:]:
    print(p.replace(os.getcwd(), '.')) # Shorten dirname

print()
import mymodule