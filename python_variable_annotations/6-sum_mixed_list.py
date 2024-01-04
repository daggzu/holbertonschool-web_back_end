#!/usr/bin/env python3

""" Module creates type-annotated function that takes a list of floats
and returns their sum as a float."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
     """function that returns the sum of float list"""
     return sum(mxd_lst)

