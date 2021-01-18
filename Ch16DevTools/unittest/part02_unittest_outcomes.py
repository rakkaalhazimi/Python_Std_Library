"""
Tests have three possible outcomes, as described in Table 16.1. There is no explicit way
to cause a test to “pass,” so a test’s status depends on the presence (or absence) of an
exception.
"""

import unittest

class OutcomeTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.assertFalse(True)

    def testError(self):
        raise RuntimeError("Test Error !")


