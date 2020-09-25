# finditer() returns an iterator that produces Match instances instead of the strings returned
# by findall().

import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
	s = match.start()
	e = match.end()
	found = match.group(0)
	print('Found {!r} at {:d}:{:d}'.format(
		text[s:e], s, e))
	print("{}".format(found))
