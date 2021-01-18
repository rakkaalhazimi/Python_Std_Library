"""
Although the return value acts like a tuple, it is really based on a namedtuple, a subclass
of tuple that supports accessing the parts of the URL via named attributes as well as
indexes. In addition to being easier to use for the programmer, the attribute API offers
access to several values not available in the tuple API.
"""

from urllib.parse import urlparse

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
print('scheme :', parsed.scheme)
print('netloc :', parsed.netloc)
print('path :', parsed.path)
print('params :', parsed.params)
print('query :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname)
print('port :', parsed.port)

"""
The username and password are available when present in the input URL, and set to
None when not. The hostname is the same value as netloc, in all lowercase and with the
port value stripped. The port is converted to an integer when present and None when not.
"""