"""
A regular tuple containing strings can be combined into a URL with urlunparse().
"""

from urllib.parse import urlparse, urlunparse
original = 'http://netloc/path;param?query=arg#frag'

print('ORIG :', original)
parsed = urlparse(original)

print('PARSED:', type(parsed), parsed)
t = parsed[:]

print('TUPLE :', type(t), t)
print('NEW :', urlunparse(t))

"""
While the ParseResult returned by urlparse() can be used as a tuple, this example explicitly
creates a new tuple to show that urlunparse() works with normal tuples, too.
"""