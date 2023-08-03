"""
This module contains  a type-annotated function concat that takes a string str1
and a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    The `concat` function takes two strings as input and returns
    their concatenation.

    :param str1: The first string that you want to concatenate
    :type str1: str
    :param str2: The parameter `str2` is a string that represents
                 the second string to be concatenated
    :type str2: str
    :return: the concatenation of `str1` and `str2`.
    """
    return str1 + str2
