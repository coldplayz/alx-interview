#!/usr/bin/python3
"""
Main file for testing
"""
import sys

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange([3, 6, 9], 1278652))
