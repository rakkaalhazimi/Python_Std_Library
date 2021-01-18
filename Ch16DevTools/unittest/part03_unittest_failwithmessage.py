"""
In the previous example, testFail() fails and the traceback shows the line with the failure
code. It is up to the person reading the test output to look at the code and figure out the
meaning of the failed test, though.
"""

import unittest

class FailureMessageTest(unittest.TestCase):

    def testFail(self):
        self.assertFalse(True, "Failure message goes here")


"""
To make it easier to understand the nature of a test failure, the fail*() and assert*()
methods accept an argument msg, which can be used to produce a more detailed error
message.
"""