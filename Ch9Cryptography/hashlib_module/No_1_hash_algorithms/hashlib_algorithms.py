"""
Since hashlib is “backed” by OpenSSL, all of the algorithms provided by that library are
available, including the following:
• MD5
• SHA1
• SHA224
• SHA256
• SHA384
• SHA512
Some algorithms are available on all platforms, and some depend on the underlying
libraries. For lists of each, look at algorithms_guaranteed and algorithms_available, respectively.
"""

import hashlib

print("Guaranted:\n{}\n".format(
    ", ".join(sorted(hashlib.algorithms_guaranteed))
))
print("Available:\n{}\n".format(
    ", ".join(sorted(hashlib.algorithms_available))
))