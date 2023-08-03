#!/usr/bin/env python3
"""
This module contains a type-annotated function to_kv that takes a
string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element is
the square of the int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    The function "to_kv" takes a key (k) and a value (v) as input, and
    returns a tuple containing the key and the square of the value.

    :param k: A string representing the key of the key-value pair
    :type k: str
    :param v: The parameter `v` can be either an integer or a float
    :type v: Union[int, float]
    :return: a tuple containing the input key `k` and the square of
             the input value `v`.
    """
    output = []
    square_v: float = lambda x: x ** 2
    output.append(k)
    output.append(square_v(v))
    return tuple(output)
