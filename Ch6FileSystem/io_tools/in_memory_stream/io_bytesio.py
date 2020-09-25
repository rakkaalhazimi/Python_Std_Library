"""
To work with raw bytes instead of Unicode text, use BytesIO.
"""

import io

# Write to a buffer
output = io.BytesIO()
output.write("This goes into the buffer.".encode("utf-8"))
output.write("ÁÇÊ'".encode('utf-8'))

# Retrieve the value written
print(output.getvalue())

output.close() # Discard buffer memory

# Initialize read buffer
input = io.BytesIO(b"Initial value for read buffer")

# Read from the buffer
print(input.read())

"""
The values written to the BytesIO instance must be bytes rather than str.
"""