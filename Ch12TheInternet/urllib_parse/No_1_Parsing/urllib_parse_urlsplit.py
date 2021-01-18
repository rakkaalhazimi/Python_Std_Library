"""
The urlsplit() function is an alternative to urlparse(). It behaves a little differently,
because it does not split the parameters from the URL. This is useful for URLs following
RFC 2396,1 which supports parameters for each segment of the path.
"""

from urllib.parse import urlsplit

url = 'http://user:pwd@NetLoc:80/p1;para/p2;para?query=arg#frag'
parsed = urlsplit(url)

print(parsed)
print('scheme :', parsed.scheme)
print('netloc :', parsed.netloc)
print('path :', parsed.path)
print('query :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname)
print('port :', parsed.port)

"""
Since the parameters are not split out, the tuple API will show five elements instead of
six, and there is no params attribute.
"""