"""
Although the point of using multiple threads is to run separate operations concurrently,
sometimes it is important to be able to synchronize the operations in two or more threads.
Event objects are a simple way to communicate between threads safely. An Event manages
an internal flag that callers can control with the set() and clear() methods. Other threads
can use wait() to pause until the flag is set, effectively blocking progress until those threads
are allowed to continue.
"""

import logging
import threading
import time


def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug("wait_for_event starting")
    event_is_set = e.wait() # pause until flag is set
    logging.debug("event set: %s", event_is_set)


def wait_for_timeout_event(e, t):
    """Wait t seconds and then timeout"""
    while not e.is_set():
        logging.debug("wait_for_event_timeout starting")
        event_is_set = e.wait(t) # pause until timeout
        logging.debug("event_set: %s", event_is_set)
        if event_is_set:
            logging.debug("processing event")
        else:
            logging.debug("doing other work")


logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)

e = threading.Event()
t1 = threading.Thread(
    name="block",
    target=wait_for_event,
    args=(e,),
)
t1.start()

t2 = threading.Thread(
    name="nonblock",
    target=wait_for_timeout_event,
    args=(e, 2),
)
t2.start()

logging.debug("Waiting before calling Event.set()")
time.sleep(5)
e.set()
logging.debug("Event is set")

"""
The wait() method takes an argument representing the number of seconds to wait for
the event before timing out. It returns a boolean value indicating whether the event is set,
so the caller knows why wait() returned. The is_set() method can be used separately on
the event without fear of blocking.
In this example, wait_for_event_timeout() checks the event status without blocking
indefinitely. The wait_for_event() blocks on the call to wait(), which does not return until
the event status changes.
"""
