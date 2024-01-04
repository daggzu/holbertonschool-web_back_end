#!/usr/bin/env python3
"""Module creates type-annotated function that takes a float argument
and returns the floor of the float."""
import math

def floor(n=float) -> int:
    """function that returns the floor of n"""
    return math.floor(n)
