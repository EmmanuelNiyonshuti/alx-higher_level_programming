#!/usr/bin/python3
""" returns a tuple with the length of a string and its first character."""


def multiple_returns(sentence):

    if not sentence:
        return (0, None)

    new_str = tuple(sentence)

    return (len(new_str), new_str[0])
