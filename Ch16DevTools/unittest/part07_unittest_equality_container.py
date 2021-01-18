"""
In addition to the generic assertEqual() and assertNotEqual() methods, special methods
are available for comparing containers such as list, dict, and set objects.
"""

import textwrap
import unittest

class ContainerEqualityTest(unittest.TestCase):

    def testCount(self):
        self.assertCountEqual(
            [1, 2, 3, 2],
            [1, 3, 2, 3]
        )

    def testDict(self):
        self.assertDictEqual(
            {"a": 1, "b": 2},
            {"a": 1, "b": 3}
        )

    def testList(self):
        self.assertListEqual(
            [1, 2, 3],
            [1, 3, 2]
        )

    def testMultiLineString(self):
        self.assertMultiLineEqual(
            textwrap.dedent("""
            This string
            has more than one
            line.
            """),
            textwrap.dedent("""
            This string has
            more than two
            lines.
            """)
        )

    def testSequence(self):
        self.assertSequenceEqual(
            [1, 2, 3],
            [1, 3, 2]
        )

    def testSet(self):
        self.assertSetEqual(
            set([1, 2, 3]),
            set([1, 2, 3, 4])
        )

    def testTuple(self):
        self.assertTupleEqual(
            (1, "a"),
            (1, "b")
        )

"""
Each of these methods reports inequality using a format that is meaningful for the input
type, thereby making test failures easier to understand and correct.
"""