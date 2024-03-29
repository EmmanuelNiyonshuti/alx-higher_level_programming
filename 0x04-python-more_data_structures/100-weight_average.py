#!/usr/bin/python3
"""Returns the weighted average of all integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):

    if not my_list:
        return 0
    sum_products = sum(score * weight for score, weight in my_list)

    sum_weights = sum(weight for _, weight in my_list)

    if sum_weights != 0:
        average = sum_products / sum_weights
        return average
    else:
        return 0
