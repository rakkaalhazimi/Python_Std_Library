"""
In addition to synchronizing the operations of threads, it is important to be able to control
access to shared resources to prevent corruption or missed data. Python’s built-in data
structures (e.g., lists, dictionaries) are thread-safe as a side effect of having atomic bytecodes
for manipulating them (the global interpreter lock that protects Python’s internal data
structures is not released in the middle of an update). Other data structures implemented
in Python, or simpler types like integers and floats, do not have that protection. To guard
against simultaneous access to an object, use a Lock object.

Procedure = acquire lock > do the work > release the lock > wait for the lock > repeat
"""

import logging
import random
import threading
import time


class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug("Waiting for lock")
        self.lock.acquire()
        try:
            logging.debug("Acquired lock")
            self.value = self.value + 1
        finally:
            self.lock.release() # Without it, the thread will block
        logging.debug("Current Count: %d", self.value)


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug("Sleeping %0.02f", pause)
        time.sleep(pause)
        c.increment()
    logging.debug("Done")

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s"
)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug("Waiting for worker threads")
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug("Counter: %d", counter.value)

"""
In this example, the worker() function increments a Counter instance, which manages a
Lock to prevent two threads from changing its internal state at the same time. If the Lock
was not used, a change to the value attribute might potentially be missed.
"""
