#!/usr/bin/python3
"""
This module comprises a function that prints a text
based on conditions.
"""

def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?', ':'

    args:
    text: text to be printed.

    Return:
    Nothing

    raises:
    TypeError when text is not an integer.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
