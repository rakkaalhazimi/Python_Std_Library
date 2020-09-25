# The struct module includes functions for converting between strings of bytes and native
# Python data types such as numbers and strings.

import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f') # integer, string , float
packed_data = s.pack(*values)
print('Original values:', values)
print('Format string :', s.format)
print('Uses :', s.size, 'bytes')
print('Packed Value :', binascii.hexlify(packed_data))