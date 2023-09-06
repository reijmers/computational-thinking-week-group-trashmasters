"""
This module is used to test student-written functions bnoth for feedback and assessment.
It is written because the built-in module unittest is not intended for ipython notebook usage, or for step-wise checking of student written functions.
"""

from typing import Callable
from math import isclose

class ReplaceThisWithYourCode():
    def __init__(self) -> None:
        pass

class TestCase():

    #grade_weight = 1
    all_tests_passed = True

    def __init__(self, tested_func: Callable = None, **kwargs):
        self.tested_func = tested_func
        self.kwargs = kwargs

    def eval(self):
        """ This function runs the test(s) and then returns the result."""
        self.test()
        return self.all_tests_passed

    def test(self) -> None:
        """ This function is intended to be overridden with the actual test. """
        pass

    def output_type(self, input, expected_output_types):
        """ Tests that the output of a function is one of the provided expected output types.
        Note that a list passed for expected output types represents multiple options, not a retun tuple."""
        real_output = self.tested_func(input)
        if not isinstance(expected_output_types, list):
            expected_output_types = [expected_output_types]
        
        if type(real_output) in expected_output_types:
            return
        else:
            print(f'Test for {self.tested_func.__name__} failed: Function should return {str(expected_output_types).replace(",", " or")} but instead returned {type(real_output)}.')
            self.all_tests_passed = False

    def io_pair(self, input, expected_output, approximate=False):
        real_output = self.tested_func(input)
        assertion = TestCase.AssertEquals if not approximate else TestCase.AssertEqualsApproximate
        if assertion(real_output, expected_output):
            return
        else:
            print(f'Test for {self.tested_func.__name__} failed: Input {input} should return {expected_output} but instead returned {real_output}.')
            self.all_tests_passed = False

    @staticmethod
    def AssertEquals(a, b):
        return a == b

    @staticmethod
    def AssertEqualsApproximate(a, b):
        return isclose(a, b)
    
    @staticmethod
    def AssertLargerThan(a, b):
        return a > b

class TestSuite():

    test_cases = []
    all_tests_passed = True

    def __init__(self, tested_func: Callable = None, **kwargs):
        self.tested_func = tested_func
        for test_case in self.test_cases:
            result = test_case(tested_func, **kwargs).eval()
            if not result:
                self.all_tests_passed = False
        if self.all_tests_passed:
            print('All tests passed')