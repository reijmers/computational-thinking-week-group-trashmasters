import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utility', 'edutest'))
import edutest

class Test_Exercise_Values(edutest.TestCase):
    def test(self):
        self.io_pair(('00:01', 5, '1990-01-01', 3, 1, 'Emma', 9, 'a+b'), 3.5190509710811696e+16)
        self.io_pair(('00:02', 6, '1990-01-02', 4, 2, 'Emma', 8, 'b+c'), 1.6897595679400317e+17)
        self.io_pair(('00:03', 7, '1990-01-03', 5, 3, 'Emma', 7, 'd*e'), 2.1272497207141005e+17)

class Test_Exercise(edutest.TestSuite):
    test_cases = [
        Test_Exercise_Values
    ]