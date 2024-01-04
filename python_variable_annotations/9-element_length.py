#!/usr/bin/env python3
"""
Module annotates function's parameters and return values with
the appropriate types.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function returns list of tuples, one for each element in lst,
        containing the element and its length. """
    return [(i, len(i)) for i in lst]
