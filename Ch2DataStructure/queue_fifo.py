import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print("Number {} out,".format(q.get()), end=" ")
    print(q.queue)
    print()

print("All done")