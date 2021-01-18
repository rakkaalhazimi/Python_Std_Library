"""
It is frequently useful to be able to skip a test if some external condition is not met. For example,
if writing tests to check the behavior of a library under a specific version of Python, there
is no reason to run those tests under other versions of Python. Test classes and methods can
be decorated with skip() to always skip the tests. The decorators skipIf() and skipUnless()
can be used to check a condition before skipping tests.
"""

import sys
import unittest

class SkippingTest(unittest.TestCase):

    @unittest.skip("always skipped")
    def test(self):
        self.assertTrue(False)

    @unittest.skipIf(sys.version_info[0] > 2,
                     "only runs on python 2")
    def test_python2_only(self):
        self.assertTrue(False)

    @unittest.skipUnless(sys.platform == "Darwin",
                         "only runs on macOS")
    def test_macos_only(self):
        self.assertTrue(False)

    def test_raise_skiptest(self):
        raise unittest.SkipTest("skipping via exception")


"""
For complex conditions that are difficult to express in a single expression to be passed
to skipIf() or skipUnless(), a test case may raise SkipTest directly to cause the test to
be skipped.
"""