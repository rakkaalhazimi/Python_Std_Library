"""
To calculate the MD5 hash, or digest, for a block of data (here a Unicode string converted
to a byte string), first create the hash object, then add the data, and finally call digest()
or hexdigest().
"""

import hashlib

with open("../hash_data.txt", "rt") as file:
    lorem = file.read()

hasher = hashlib.md5()
hasher.update(lorem.encode("utf-8"))
print(hasher.hexdigest())