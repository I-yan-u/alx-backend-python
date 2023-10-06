#!/usr/bin/env python3
""" annotations of complex types"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of float values and returns the sum
        input_list (List[float]): The list of float values
        return (float): sum
    """
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
