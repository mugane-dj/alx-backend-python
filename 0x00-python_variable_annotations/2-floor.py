#!/usr/bin/env python3
import math
"""
This module contains a type-annotated function floor which
takes a float n as argument and returns the floor of the float.
"""


def floor(n: float) -> int:
    """
    The function `floor` takes a float number as input and returns
    the largest integer less than or equal to the input.

    :param n: A float number that we want to find the floor value of
    :type n: float
    :return: the floor value of the input number.
    """
    return math.floor(n)
