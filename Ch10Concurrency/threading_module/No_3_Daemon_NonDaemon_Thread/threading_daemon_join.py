"""
To wait until a daemon thread has completed its work, use the join() method.
"""

import threading
import logging
import time


def daemon():
    logging.debug("Starting")
    time.sleep(0.2)
    logging.debug("Exiting")


def non_daemon():
    logging.debug("Starting")
    logging.debug("Exiting")


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name="daemon", target=daemon, daemon=True)
t = threading.Thread(name="non-daemon", target=non_daemon)

d.start()
t.start()

d.join()
t.join()

"""
Waiting for the daemon thread to exit using join() means it has a chance to produce its
"Exiting" message.
"""