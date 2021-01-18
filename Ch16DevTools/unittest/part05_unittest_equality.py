"""
As a special case, unittest includes methods for testing the equality of two values.
"""

import unittest

class EqualityTest(unittest.TestCase):

    def testExpectEqual(self):
        self.assertEqual(1, 3 - 2)

    def testExpectEqualFail(self):
        self.assertEqual(2, 3 - 2)

    def testExpectNotEqual(self):
        self.assertNotEqual(2, 3 - 2)

    def testExpectNotEqualFail(self):
        self.assertNotEqual(1, 3 - 2)


"""
When they fail, these special test methods produce error messages that identify the values
being compared.
"""