#!/usr/bin/python3

"""list_division - divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):

    result_list = []

    for i in range(list_length):
        result = 0

        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                raise TypeError("wrong type")

            result = element_1 / element_2
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            result_list.append(result)

    return result_list
