"""
Raw byte streams such as sockets can be wrapped with a layer to handle string encoding and
decoding, making it easier to use them with text data. The TextIOWrapper class supports
both writing and reading. The write_through argument disables buffering, and flushes all
data written to the wrapper through to the underlying buffer immediately.
"""

import io

# Write to a buffer
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding="utf-8",
    write_through=True,
)
wrapper.write("This goes into buffer. ")
wrapper.write("ÁÇÊ")

# Retrive the value written.
print(output.getvalue())

# output.close() # Discard buffer memory.
#
# # Initialize read buffer.
# input = io.BytesIO(
#     b"Initial value for read buffer with unicode characters " +
#     "ÁÇÊ".encode("utf-8")
# )
# wrapper = io.TextIOWrapper(input, encoding="utf-8")
#
# # Read from buffer.
# print(wrapper.read())

"""
This example uses a BytesIO instance as the stream. Examples for bz2 (page 491),
http.server (page 781), and subprocess (page 535) demonstrate using TextIOWrapper with
other types of file-like objects.
"""


