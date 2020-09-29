"""
Because the args and kwargs values passed to the Thread constructor are saved in private
variables using names prefixed with '__', they are not easily accessed from a subclass. To
pass arguments to a custom thread type, redefine the constructor to save the values in an
instance attribute that can be seen in the subclass.
"""

import threading
import logging

class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug("running with %s and %s",
                      self.args, self.kwargs)

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s"
)

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={"a": "A", "b": "B"})
    t.start()

"""
MyThreadWithArgs uses the same API as Thread, but another class could easily change
the constructor method to take more or different arguments more directly related to the
purpose of the thread, as with any other class.
"""    