"""
Use assertIn() to test container membership.
"""

import unittest

class ContainerMembershipTest(unittest.TestCase):

    def testDict(self):
        self.assertIn(4, {1: "a", 2: "b", 3: "c"})

    def testList(self):
        self.assertIn(4, [1, 2, 3])

    def testSet(self):
        self.assertIn(4, set([1, 2, 3]))


"""
Any object that supports the in operator or the container API can be used with assertIn().
"""