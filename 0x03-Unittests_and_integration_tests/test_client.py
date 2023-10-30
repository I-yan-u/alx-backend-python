#!/usr/bin/env python3
"""
Unittest file
"""
import unittest
from utils import access_nested_map, get_json, memoize
import client
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient
    """
    @parameterized.expand([
        ('google', {'payload': True}),
        ('abc', {'payload': False})
    ])
    @patch('client.get_json')
    def test_org(self, org, data, mock_get_json):
        """
        Test GithubOrgClient.org
        """
        gitClient = GithubOrgClient(org)
        mock_get_json.return_value = MagicMock(return_value=data)
        self.assertEqual(gitClient.org(), data)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org)
        )


if __name__ == "__main__":
    unittest.main()
