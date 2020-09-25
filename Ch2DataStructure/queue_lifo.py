import queue

q = queue.LifoQueue()

for i in range(5):
    q.put(i)

print("The queue is {}, we will use Last In First Out".format(q.queue))
print()

while not q.empty():
    print("Number {} out,".format(q.get()), end=" ")
    print(q.queue)
    print()

print("All done")