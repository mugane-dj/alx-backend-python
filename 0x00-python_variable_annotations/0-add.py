#!/usr/bin/env python3
"""
This module contains a type-annotated function add that takes a
float a and a float b as arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """
    The function "add" takes two float numbers as input
    and returns their sum as a float.

    :param a: float - This parameter represents the first number to be added
    :type a: float
    :param b: The parameter "b" is a float, which means it can
              accept decimal numbers as input
    :type b: float
    :return: the sum of the two input numbers, a and b.
    """
    return a + b
