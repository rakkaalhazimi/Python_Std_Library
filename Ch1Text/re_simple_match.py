# The search() function takes
# the pattern and text to scan, and returns a Match object when the pattern is found. If the
# pattern is not found, search() returns None.

# Each Match object holds information about the nature of the match, including the original
# input string, the regular expression used, and the location within the original string
# where the pattern occurs.

import re

pattern = r'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
	match.re.pattern, match.string, s, e, text[s:e]))
