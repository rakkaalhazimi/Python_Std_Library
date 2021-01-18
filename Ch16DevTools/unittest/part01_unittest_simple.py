"""
Tests, as defined by unittest, have two parts: code to manage test dependencies (called
fixtures) and the test itself. Individual tests are created by subclassing TestCase and overriding
or adding appropriate methods. In the following example, the SimplisticTest has a
single test() method, which would fail if a is ever different from b.
"""

import unittest

class SimplicisticTest(unittest.TestCase):

   def test(self):
       a = "a"
       b = "a"
       self.assertEqual(a, b)


"""
The easiest way to run unittest tests is use the automatic discovery available through the
command-line interface.

python -m unittest unittest_simple.py

This abbreviated output includes the amount of time the tests took, along with a status
indicator for each test (the . on the first line of output means that a test passed). For more
detailed test results, include the -v option.
 
python -m unittest -v unittest_simple.py
"""