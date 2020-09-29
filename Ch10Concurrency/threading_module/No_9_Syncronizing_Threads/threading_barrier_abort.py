"""
The abort() method of Barrier causes all of the waiting threads to receive a
BrokenBarrierError. This allows threads to clean up if processing stops while they are
blocked on wait().
"""

import threading
import time


def worker(barrier):
    print(threading.current_thread().name,
          "waiting for barrier with {} others".format(
              barrier.n_waiting))
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, "aborting")
    else:
        print(threading.current_thread().name, "after barrier",
              worker_id)

NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
    threading.Thread(
        name="worker-%s" % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, "starting")
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()

"""
This example configures the Barrier to expect one more participating thread than is
actually started so that processing in all of the threads is blocked. The abort() call raises
an exception in each blocked thread.
"""