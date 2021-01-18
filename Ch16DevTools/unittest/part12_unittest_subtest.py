"""
It is frequently useful to run the same test logic with different inputs. Rather than defining
a separate test method for each small case, a commonly used technique is to create one test
method containing several related assertion calls. The problem with this approach is that
as soon as one assertion fails, the rest are skipped. A better solution is to use subTest() to
create a context for a test within a test method. If the test then fails, the failure is reported
and the remaining tests continue.
"""

import unittest

class SubTest(unittest.TestCase):

    def test_combined(self):
        self.assertRegex("abc", "a")
        self.assertRegex("abc", "B")
        # The next assertions are not verified!
        self.assertRegex("abc", "c")
        self.assertRegex("abc", "d")

    def test_with_subtest(self):
        for pat in ["a", "B", "c", "d"]:
            with self.subTest(pattern=pat):
                self.assertRegex("abc", pat)


"""
In this example, the test_combined() method never runs the assertions for the patterns
'c' and 'd'. The test_with_subtest() method does, and correctly reports the additional
failure. Note that the test runner still perceives that only two test cases exist, even though
three failures are reported.
"""