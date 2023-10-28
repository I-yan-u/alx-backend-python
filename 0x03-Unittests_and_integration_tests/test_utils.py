#!/usr/bin/env python3
"""
Unittest file
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittest class to check nested map access
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, result):
        self.assertEqual(access_nested_map(map, path), result)


if __name__ == "__main__":
    unittest.main()
