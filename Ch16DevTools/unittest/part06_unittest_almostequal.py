"""
In addition to strict equality, it is possible to test for near equality of floating-point numbers
using assertAlmostEqual() and assertNotAlmostEqual().
"""

import unittest

class AlmostEqualTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1.1, 3.3 - 2.2)

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3 - 2.2, places=1)

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)


"""
The arguments are the values to be compared and the number of decimal places to use for
the test.
"""