#!/usr/bin/python3
""" returns a tuple with the length of a string and its first character."""


def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    new_str = tuple(sentence)
    n = len(new_str)
    first = new_str[0]

    return (n, first)
