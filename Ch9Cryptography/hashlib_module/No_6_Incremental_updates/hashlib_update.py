"""
The update() method of the hash calculators can be called repeatedly. Each time, the digest
is updated based on the additional text fed in. Updating incrementally is more efficient than
reading an entire file into memory, and produces the same results.
"""

import hashlib

with open("../hash_data.txt", "rt") as file:
    lorem = file.read()
    print(file)

hash = hashlib.md5()
hash.update(lorem.encode("utf-8"))
all_at_once = hash.hexdigest()

def chunksize(size, text):
    "Return parts of the text in size-based increments"
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return

hash = hashlib.md5()
for chunk in chunksize(64, lorem.encode("utf-8")):
    hash.update(chunk)
line_by_line = hash.hexdigest()

print("All at once  :", all_at_once)
print("Line by line :", line_by_line)
print("Same         :", all_at_once == line_by_line)