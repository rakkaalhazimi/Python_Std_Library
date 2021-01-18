"""
Rather than deleting tests that are persistently broken, these tests can be marked with the
expectedFailure() decorator so that their failure is ignored.
"""

import unittest

class Test(unittest.TestCase):

    @unittest.expectedFailure
    def test_never_passes(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_always_passed(self):
        self.assertTrue(True)