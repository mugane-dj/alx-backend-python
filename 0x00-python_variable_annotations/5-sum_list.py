from functools import reduce
"""
This module contains a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    The function `sum_list` takes a list of floats as input and
    returns the sum of all the elements in the list.

    :param input_list: The input_list parameter is a list of floating-point
                       numbers
    :type input_list: list[float]
    :return: The function `sum_list` returns the sum of all the elements
             in the input list.
    """
    return reduce(lambda x, y: x + y, input_list)
