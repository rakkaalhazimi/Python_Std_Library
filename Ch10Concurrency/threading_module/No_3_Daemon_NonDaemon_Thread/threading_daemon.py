"""
Up to this point, the example programs have implicitly waited to exit until all threads have
completed their work. Sometimes, however, programs spawn a thread as a daemon that runs
without blocking the main program from exiting. Daemon threads are useful for services
where there may not be an easy way to interrupt the thread, or where letting the thread
die in the middle of its work does not lead to loss or corruption of data (for example, a
thread that generates “heart-beats” for a service monitoring tool). To mark a thread as a
daemon, pass daemon=True when constructing it or call its set_daemon() method with True.
The default is for threads to not be daemons.
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

"""
The output from this code does not include the "Exiting" message from the daemon
thread, since all of the non-daemon threads (including the main thread) exit before the
daemon thread wakes up from the sleep() call.
"""