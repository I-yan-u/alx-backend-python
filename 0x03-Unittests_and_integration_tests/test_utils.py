#!/usr/bin/env python3
"""
Unittest file
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


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


class TestMemoize(unittest.TestCase):
    """
    Test utils.memoize function
    """
    def test_memoize(self):
        """ test memoize method """
        class TestClass:
            """ Testclass """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
