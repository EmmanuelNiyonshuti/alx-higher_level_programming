#!/usr/bin/python3
"""This module comprises a function that prints a text"""

def text_indentation(text):
    """Prints a text with  2 new lines after each of ., ? and :.

    parameter:
    text: the string to be printed.

    raises a TypeError with message when text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
