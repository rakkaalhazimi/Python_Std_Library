"""
In addition to using Events, another way of synchronizing threads is by using a Condition
object. Because the Condition uses a Lock, it can be tied to a shared resource, allowing
multiple threads to wait for the resource to be updated. In the next example, the consumer()
threads wait for the Condition to be set before continuing. The producer() thread is
responsible for setting the condition and notifying the other threads that they can
continue.
"""

import logging
import threading
import time


def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug("Starting consumer thread")
    with cond:
        cond.wait() # waiting to be notified
        logging.debug("Resouce is available to consumer")


def produces(cond):
    """set up the resource to be used by the cunsomer"""
    logging.debug("Starting producer thread")
    with cond:
        logging.debug("Making resource available")
        cond.notifyAll() # wakes up other thread


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s (%(threadName)-2s) %(message)s",
)

condition = threading.Condition()
c1 = threading.Thread(name="c1", target=consumer,
                      args=(condition,))
c2 = threading.Thread(name="c2", target=consumer,
                      args=(condition,))
p = threading.Thread(name="p", target=produces,
                     args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

"""
The threads use with to acquire the lock associated with the Condition. Using the acquire()
and release() methods explicitly also works.
"""
