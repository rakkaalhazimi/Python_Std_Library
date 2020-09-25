"""
In a dynamically typed language like Python, there is often a need to perform slightly
different operations based on the type of an argument, especially when dealing with the
difference between a list of items and a single item.

functools provides the singledispatch() decorator to register a set
of generic functions for automatic switching based on the type of the first argument to a
function.
"""

import functools

@functools.singledispatch
def myfunc(arg):
    print("This is my string {!r}".format(arg))

@myfunc.register(int)
def myfunc_int(arg):
    print("Hey my favorite number is {}".format(arg))

@myfunc.register(list)
def myfunc_list(arg):
    print("This is my waifus {}".format(arg))

myfunc("rakka")
myfunc(7)
myfunc(["Lappland", "Skadi"])