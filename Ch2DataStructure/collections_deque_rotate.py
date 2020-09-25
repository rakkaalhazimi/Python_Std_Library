import collections

d = collections.deque(range(10))
print("Normal\n", d)

d = collections.deque(range(10))
d.rotate(2)
print("Right Rotation\n", d)

d = collections.deque(range(10))
d.rotate(-2)
print("Left Rotation\n", d)