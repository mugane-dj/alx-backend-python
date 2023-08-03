#!/usr/bin/env python3
"""
This module contains  a type-annotated function to_str that takes a float n
as argument and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """
    The function `to_str` converts a float number to a string representation.

    :param n: a float number
    :type n: float
    :return: a string representation of the input float number.
    """
    return n.__str__()
