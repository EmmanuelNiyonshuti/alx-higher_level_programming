#!/usr/bin/python3
"""Operators of overriding"""


class MyInt(int):
    """Overrides '==' and '!=' operators"""

    def __eq__(self, other):
        """Overriding '=='"""
        return False

    def __ne__(self, other):
        """overriding '!='"""
        return True
