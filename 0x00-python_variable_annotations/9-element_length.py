"""
This module contains an annotated function element_length that takes an
iterable as an argument and returns a list of tuples representing the
elements in the list and their length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    The function `element_length` takes a list of sequences as input and
    returns a list of tuples, where each tuple contains a sequence from
    the input list and its corresponding length.

    :param lst: An iterable of sequences
    :type lst: Iterable[Sequence]
    :return: The function `element_length` returns a list of tuples.
             Each tuple contains two elements:the original sequence
             from the input list `lst`, and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
