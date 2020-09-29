"""
Using arguments to identify or name the thread is cumbersome and unnecessary. Each
Thread instance has a name with a default value that can be changed as the thread is
created. Naming threads is useful in server processes in which multiple service threads
handle different operations.
"""

import threading
import time

def worker():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.2)
    print(threading.current_thread().getName(), "Exiting")

def my_service():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.3)
    print(threading.current_thread().getName(), "Exiting")

t = threading.Thread(name="my_service", target=my_service)
w = threading.Thread(name="worker", target=worker)
w2 = threading.Thread(target=worker) # Use default name

w.start()
w2.start()
t.start()

"""
The debug output includes the name of the current thread on each line. The lines with
"Thread-1" in the thread name column correspond to the unnamed thread w2.
"""