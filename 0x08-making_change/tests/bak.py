#!/usr/bin/python3
"""Test module for task 0.
"""
from unittest import TestCase
from parameterized import parameterized
from typing import Mapping, Dict, List, Tuple, Sequence, Any, Callable
import io
import sys

makeChange = __import__('0-making_change').makeChange

INPUTS: List[Tuple] = [
        ("empty list, positive total", [], 50, '-1\n'),
        ([], 0, '0\n'),
        ([], -11, '0\n'),
        ([8, 9, 4, 72, 2647], 2740, '5\n'),
        ([4, 971, 5, 81, 1], 1084, '11\n'),
        ([261, 58, 94], 417, '-1\n'),
        ]


class TestMakeChange(TestCase):
    """ Tests for the task 0.
    """
    @parameterized.expand(INPUTS)
    def test_makeChange(self, coins, total, expectation):
        """ Test for expected output.
        """
        # capture terminal output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        makeChange(coins, total)
        sys.stdout = sys.__stdout__

        # test
        self.assertEqual(captured_output.getvalue(), expectation)
