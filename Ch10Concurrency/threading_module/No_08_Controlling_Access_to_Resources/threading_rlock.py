"""
In a situation where separate code from the same thread needs to “reacquire” the lock, use
an RLock instead.
"""

import threading

lock = threading.RLock()

print("First try :", lock.acquire())
print("Second try :", lock.acquire(0))

"""
The only change to the code from the previous example was substituting RLock for Lock.
"""
