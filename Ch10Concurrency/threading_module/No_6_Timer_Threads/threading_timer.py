"""
One example of a reason to subclass Thread is provided by Timer, which is also included in
threading. A Timer starts its work after a delay, and can be canceled at any point within
that delay time period.
"""

import threading
import time
import logging


def delayed():
    logging.debug("worker running")

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)

t1 = threading.Timer(0.3, delayed)
t1.setName("t1")
t2 = threading.Timer(0.3, delayed)
t2.setName("t2")

logging.debug("starting timers")
t1.start()
t2.start()

logging.debug("waiting before cancelling %s", t2.getName())
time.sleep(0.2)
logging.debug("cancelling %s", t2.getName())
t2.cancel()
logging.debug("done")

"""
The second timer in this example never runs, and the first timer appears to run after
the rest of the main program is done. Since it is not a daemon thread, it is joined implicitly
when the main thread is done.
"""