"""
The weakref module supports weak references to objects.

A normal reference increments the
reference count on the object and prevents it from being garbage collected. This outcome is
not always desirable, especially when a circular reference might be present or when a cache
of objects should be deleted when memory is needed.

Weak references to objects are managed through the ref class. To retrieve the original
object, call the reference object.
"""

import weakref

class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))

obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())

"""
In this case, since obj is deleted before the second call to the reference, the ref returns
None.
"""