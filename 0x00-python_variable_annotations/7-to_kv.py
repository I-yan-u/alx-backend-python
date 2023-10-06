#!/usr/bin/env python3
""" complex type annotations """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """
    Complex type annotations
        k (str): String
        v ([int, float]): int | float
        return: tuple
    """
    return k, v ** 2
