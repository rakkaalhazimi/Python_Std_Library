"""
Locks implement the context manager API and are compatible with the with statement.
Using with removes the need to explicitly acquire and release the lock.
"""

import threading
import logging


def worker_with(lock):
    with lock:
        logging.debug("Lock acquire via with")


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug("Lock acquired directly")
    finally:
        lock.release()

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s"
)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()

"""
The two functions worker_with() and worker_no_with() manage the lock in equivalent
ways.
"""