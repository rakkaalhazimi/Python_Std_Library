"""
The tearDown methods may not all be invoked if errors occur during the process of cleaning
up fixtures. To ensure that a fixture is always released correctly, use addCleanup().
"""

import random
import shutil
import tempfile
import unittest

def remove_tmdir(dirname):
    print("In remove_tmdir")
    shutil.rmtree(dirname)

class FixturesTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.tmdir = tempfile.mkdtemp()
        self.addCleanup(remove_tmdir, self.tmdir)

    def test1(self):
        print("\nIn test1()")

    def test2(self):
        print("\nIn test2()")