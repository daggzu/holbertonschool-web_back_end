#!/usr/bin/env python3

""" Module creates type-annotated function that takes a list of floats
and returns their sum as a float."""
from typing import List


def sum_list(input_list:List[float]) -> float:
    """function that returns the sum of float list"""
    return sum(input_list)
