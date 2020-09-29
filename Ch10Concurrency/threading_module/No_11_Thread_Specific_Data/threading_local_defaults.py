"""
To initialize the settings so all threads start with the same value, use a subclass and set
the attributes in __init__().
"""

import random
import threading
import logging


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug("No value yet")
    else:
        logging.debug("value=%s", val)


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

class MyLocal(threading.local):

    def __init__(self, value):
        super(MyLocal, self).__init__()
        logging.debug("Initializing %r", self)
        self.value = value


logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s"
)

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()

"""
__init__() is invoked on the same object (note the id() value) once in each thread to
set the default values.
"""