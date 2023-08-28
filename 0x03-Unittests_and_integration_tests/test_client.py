#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock, patch, PropertyMock
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
        instance = GithubOrgClient(org)
        mocked_func.return_value = MagicMock(return_value=res)
        self.assertEqual(instance.org(), res)
        mocked_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        instance = GithubOrgClient("google")
        mock_prop = PropertyMock(
            return_value={
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
        )
        with patch.object(instance.__class__, "org", mock_prop):
            self.assertEqual(
                instance._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )
