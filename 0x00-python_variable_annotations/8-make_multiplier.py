#!/usr/bin/env python3
""" complex type annotations """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Fuction that returns a multiplier function """
    def fun_multiplier(num: float) -> float:
        """ Multiplier function
            Returns: float
        """
        return multiplier * num
    return fun_multiplier
