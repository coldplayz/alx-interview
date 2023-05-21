#!/usr/bin/python3
"""
Main for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [235, 140]
print(validUTF8(data))
