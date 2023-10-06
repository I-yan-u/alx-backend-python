#!/usr/bin/env python3
""" Complex type annotations """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples containing the element
        and the length of the element
    """
    return [(i, len(i)) for i in lst]
