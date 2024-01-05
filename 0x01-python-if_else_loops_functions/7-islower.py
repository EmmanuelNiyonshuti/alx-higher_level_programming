#!/usr/bin/python3
def islower(c):
    """checks for lowercase character."""
    for i in range(ord('a'), ord('z') + 1):
        if ord(c) == i:
           return True
        else:
            return False
