#!/usr/bin/env python3
"""
Module creates type-annotated function that takes a float argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function returns function that multiplies float by multiplier """

    def multiply(n: float) -> float:
        """ Function returns product of float and multiplier """
        return n * multiplier

    return multiply
