"""
The partial object does not have __name__ or __doc__ attributes by default, and without
those attributes, decorated functions are more difficult to debug.
update_wrapper() can be
used to copy or add attributes from the original function to the partial object.
"""

import functools

def myfunc(a, b=2):
    "Docstring for myfunc()."
    print(' called myfunc with:', (a, b))

def otherfunc(a, b=3):
    "Docstring for otherfunc()"
    print(" called otherfunc with:", (a, b))

def show_details(name, f):
    "Show details of a callable object."

    print('{}:'.format(name))
    print(' object:', f)
    print(' __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print(' __doc__', repr(f.__doc__))
    print()

show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print('Updating wrapper:')
print(' assign:', functools.WRAPPER_ASSIGNMENTS) # attr added
print(' update:', functools.WRAPPER_UPDATES) # values to be modified
print()

functools.update_wrapper(p1, otherfunc)
show_details('updated wrapper', p1)