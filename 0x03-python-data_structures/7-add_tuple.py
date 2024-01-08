#!/usr/bin/python3
"""adds two turples"""


def add_tuple(tuple_a=(), tuple_b=()):

    new_a = list(tuple_a)
    new_b = list(tuple_b)


new_a[0] = new_a[0] + new_b[0]
new_b[1] = new_a[1] + new_b[1]

for i in range(2):
    if new_a[i] + new_b[i] < 2:
        new_a[i] = 0
    elif new_a[i] + new_b[i] >= 2:
        new_a[i] = 2
tuple_a = tuple(new_a)
tuple_b = tuple(new_b)

return tuple_a, tuple_b
