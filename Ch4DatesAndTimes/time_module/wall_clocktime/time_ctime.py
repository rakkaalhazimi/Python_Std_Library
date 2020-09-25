"""
For logging or printing times, ctime() can
be a better choice.
"""

import time

print('The time is :', time.ctime())
later = time.time() + 15
print('15 secs from now :', time.ctime(later))

"""
The second print() call in this example shows how to use ctime() to format a time value
other than the current time.
"""