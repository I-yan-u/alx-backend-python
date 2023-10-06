#!/usr/bin/env python3
""" annotations of complex types"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Takes a list of float values and returns the sum
        mxd_list ([int, float]): The list of float values
        return (float): sum
    """
    sum: float = 0
    for num in mxd_list:
        sum += num
    return sum
