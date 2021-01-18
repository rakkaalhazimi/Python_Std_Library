"""
There are several ways to reassemble the parts of a split URL into a single string. The
parsed URL object has a geturl() method.
"""

from urllib.parse import urlparse

original = 'http://netloc/path;param?query=arg#frag'
print('ORIG :', original)
parsed = urlparse(original)
print('PARSED:', parsed.geturl())

"""
geturl() works only on the object returned by urlparse() or urlsplit().
"""