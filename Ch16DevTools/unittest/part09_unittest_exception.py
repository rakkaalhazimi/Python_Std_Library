"""
As previously mentioned, if a test raises an exception other than AssertionError, it is
treated as an error. This behavior can be used to uncover mistakes while modifying code
that has existing test coverage. In some circumstances, however, the test should verify
that some code does produce an exception. For example, if an invalid value is given to an
attribute of an object, assertRaises() leads to clearer code than trapping the exception in
the test. The next example includes two tests that can be compared on this basis.
"""

import unittest

def raise_error(*args, **kwds):
    raise ValueError("Invalid value: ", str(args), str(kwds))

class ExceptionTest(unittest.TestCase):

    def trapLocally(self):
        try:
            raise_error("a", b="c")
        except ValueError:
            pass
        else:
            self.fail("Did not see ValueError")

    def testAssertRaises(self):
        self.assertRaises(
            ValueError,
            raise_error,
            "a",
            b="c"
        )