from functools import reduce
from typing import List, Union
"""
This module contains  a type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    The function `sum_mixed_list` takes a list of integers and floats
    and returns the sum of all the elements in the list.

    :param mxd_list: The parameter `mxd_list` is a list that can
                     contain elements of type `int` or
    `float`
    :type mxd_list: List[int | float]
    :return: the sum of all the elements in the mixed list.
    """
    return reduce(lambda x, y: x + y, mxd_list)
