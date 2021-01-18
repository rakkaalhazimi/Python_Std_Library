"""
Fixtures are the outside resources that a test needs. For example, tests for one class may
all need an instance of another class that provides configuration settings or another shared
resource. Other test fixtures include database connections and temporary files. (Many people
would argue that using external resources makes such tests not “unit” tests, but they are
still tests and still useful.)

unittest includes special hooks to configure and clean up any fixtures needed by tests.
To establish fixtures for each individual test case, override setUp() on the TestCase. To
clean them up, override tearDown(). To manage one set of fixtures for all instances of a
test class, override the class methods setUpClass() and tearDownClass() for the TestCase.
Finally, to handle especially expensive setup operations for all of the tests within a module,
use the module-level functions setUpModule() and tearDownModule().
"""

import random
import unittest

def setUpModule():
    print("In setUpModule()")

def tearDownModule():
    print("In tearDownModule()")


class FixtureTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("In setUpClass()")
        cls.good_range = range(1, 10)

    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass()")
        del cls.good_range

    def setUp(self):
        super().setUpClass()
        print("\nIn setUp()")
        # Pick a number sure to be in the range. The range is
        # defined as not including the "stop" value, so this
        # value should not be included in the set of allowed
        # values for our choice.
        self.value = random.randint(
            self.good_range.start,
            self.good_range.stop - 1,
        )

    def tearDown(self):
        print("In tearDown()")
        del self.value
        super().tearDown()

    def test1(self):
        print("In test1()")
        self.assertIn(self.value, self.good_range)

    def test2(self):
        print("In test2()")
        self.assertIn(self.value, self.good_range)


"""
When this sample test is run, the order of execution of the fixture and test methods is
apparent.
"""