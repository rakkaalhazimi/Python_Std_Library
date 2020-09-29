"""
Barriers are another thread synchronization mechanism. A Barrier establishes a control
point, and all participating threads then block until all of the participating “parties” have
reached that point. With this approach, threads can start up separately and then pause
until they are all ready to proceed.
"""

import threading
import time


def worker(barrier):
    print(threading.current_thread().name,
          "waiting for barrier with {} others".format(
              barrier.n_waiting))
    worker_id = barrier.wait()
    print(threading.current_thread().name, "after barrier",
          worker_id)

def report():
    current = threading.current_thread().name
    print("The last thread {}, has finished".format(current))

NUM_THREADS = 4

barrier = threading.Barrier(NUM_THREADS, action=report)

threads = [
    threading.Thread(
        name="worker-%s" % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, "Starting")
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()

"""
In this example, the Barrier is configured to block until three threads are waiting. When
the condition is met, all of the threads are released past the control point at the same time.
The return value from wait() indicates the number of the party being released, and can be
used to limit some threads from taking an action such as cleaning up a shared resource.
"""