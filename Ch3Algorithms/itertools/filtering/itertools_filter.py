"""
The built-in function filter() returns an iterator that includes only items for which
the test function returns true.
"""

def check_item(x):
    print('Testing:', x)
    return x < 1

for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)