#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock, patch
from typing import Dict
from parameterized import parameterized

GithubOrgClient = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests on GithubOrgClient methods
    """

    @parameterized.expand(
        [("google", {"login": "google"}), ("abc", {"login": "abc"})]
    )
    @patch("client.get_json")
    def test_org(self, org: str, res: Dict, mocked_func: MagicMock) -> None:
        """
        Test memoized func org
        """
        client = GithubOrgClient(org)
        mocked_func.return_value = MagicMock(return_value=res)
        self.assertEqual(client.org(), res)
        mocked_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
