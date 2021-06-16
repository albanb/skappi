#!/usr/bin/env python
# -*-coding:utf-8 -*
"""
Gather all tests for skappi.
"""
# pylint: disable=missing-function-docstring
# No need to add a docstring to each tests.

import sys
import unittest
import test_skappi.py

if __name__ == "__main__":
    all_tests = unittest.TestSuite(unittest.TestLoader().loadTestsFromModule(test_skappi))
    result = unittest.TextTestRunner(verbosity=2).run(all_tests)
    sys.exit(not result.wasSuccessful())
