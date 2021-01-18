"""
The return value from the urlparse() function is a ParseResult object that acts like a
tuple with six elements.
"""

from urllib.parse import urlparse

url = "http://netloc/path;param?query=arg#frag"
parsed = urlparse(url)
print(parsed)

"""
The parts of the URL available through the tuple interface are the scheme, network
location, path, path segment parameters (separated from the path by a semicolon), query,
and fragment.
"""