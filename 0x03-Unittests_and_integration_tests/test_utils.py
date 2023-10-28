#!/usr/bin/env python3
"""
Unittest file
"""
import unittest
import utils
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, MagicMock


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class on get json method
    """
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, data, mock_request):
        mock = mock_request(url)
        mock.json.return_value = data

        mock_request.assert_called_once_with(url)
        self.assertEqual(get_json(url), data)


if __name__ == "__main__":
    unittest.main()
