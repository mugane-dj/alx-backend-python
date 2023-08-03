#!/usr/bin/env python3
"""
This module contains  a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies a float
by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    The function "make_multiplier" returns a lambda function that
    multiplies a given number by a specified multiplier.

    :param multiplier: The `multiplier` parameter is a float value
                       that represents the value by which the input
                       number should be multiplied
    :type multiplier: float
    :return: a lambda function that takes a float as input and returns
             the product of that float and the multiplier.
    """
    return lambda x: x * multiplier
