"""
Most tests assert the truth of some condition. Truth-checking tests can be written in two
different ways, depending on the perspective of the test author and the desired outcome of
the code being tested.
"""

import unittest

class TruthTest(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True)

    def testAssertFalse(self):
        self.assertFalse(False)


"""
If the code produces a value that can be evaluated as true, the method assertTrue()
should be used. If the code produces a false value, the method assertFalse() makes more
sense.
"""