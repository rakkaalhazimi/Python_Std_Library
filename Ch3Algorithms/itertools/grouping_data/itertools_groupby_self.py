from itertools import *

item1 = cycle(islice(count(), 3))
item2 = islice(count(), 7)

items = [(x, y) for x, y in zip(item1, item2)]

def category(x):
    return x[0]

items.sort()
print("Items", items, sep="\n")
for key, value in groupby(items, category):
    print(key, list(value))
