#!/usr/bin/python3
"""Test module for task 0.
"""
from unittest import TestCase
from parameterized import parameterized
from typing import Mapping, Dict, List, Tuple, Sequence, Any, Callable

makeChange = __import__('0-making_change').makeChange

INPUTS: List[Tuple] = [
        ("empty list, positive total", [], 50, -1),
        ("empty list, 0 total", [], 0, 0),
        ("empty list, negative total", [], -11, 0),
        ("exact list", [8, 9, 4, 72, 2647], 2740, 5),
        ("inexact list", [4, 971, 5, 81, 1], 1084, 10),
        ("wrong list", [261, 58, 94], 417, -1),
        ]


class TestMakeChange(TestCase):
    """ Tests for the task 0.
    """
    @parameterized.expand(INPUTS)
    def test_makeChange(self, title, coins, total, expectation):
        """ Test for expected output.
        """
        output = makeChange(coins, total)

        # test
        self.assertEqual(output, expectation)
