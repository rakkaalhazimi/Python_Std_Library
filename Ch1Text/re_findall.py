# The findall() function returns all of the substrings of the input that match
# the pattern without overlapping.

import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.findall(pattern, text):
	print('Found {!r}'.format(match))
