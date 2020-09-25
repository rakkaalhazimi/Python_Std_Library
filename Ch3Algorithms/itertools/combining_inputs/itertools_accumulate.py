"""
The accumulate() function processes the input iterable, passing the nth and n+1st item
to a function and producing the return value instead of either input.
"""

from itertools import accumulate

print("Default accumulate")
print(list(accumulate(range(5))))
print(list(accumulate('abcde')))
print()

def f(a, b):
    return b + a + b

print("Custom accumulate")
print(list(accumulate(range(5), f)))
print(list(accumulate('abcde', f)))