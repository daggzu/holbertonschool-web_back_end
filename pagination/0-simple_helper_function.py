#!/usr/bin/env python3
"""
Module defines a function returns a tuple containing the start and end
document indexes to paginate the collection.
"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """Returns a tuple containing the start and end document indexes"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
