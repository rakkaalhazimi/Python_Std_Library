"""
StringIO provides a convenient means of working with text in memory using the file API
(e.g., read(), write()). Using StringIO to build large strings can offer performance savings
over some other string concatenation techniques in some cases. In-memory stream buffers
are also useful for testing, where writing to a real file on disk may slow down the test suite.
A few standard examples of using StringIO buffers follow.
"""

import io

# Write to a buffer
output = io.StringIO()
output.write("This goes into buffer. ")
print("And so does this. ", file=output)

# Retrieve the value written
print(output.getvalue())

output.close() # Discard buffer memory.

# Initialize a read buffer.
input = io.StringIO("Initial value for read buffer")

# Read from buffer
print(input.read())

"""
This example uses read(), but the readline() and readlines() methods are also available.
The StringIO class provides a seek() method for jumping around in a buffer while
reading, which can be useful for rewinding if a look-ahead parsing algorithm is being used.
"""