"""
It is useful to be able to spawn a thread and pass arguments that tell it which work to do.
Any type of object can be passed as argument to the thread. The next example passes a
number, which the thread then prints.
"""

import threading

def worker(num):
    """thread worker function"""
    print("Worker: %s" % num)

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(i)
    t.start()