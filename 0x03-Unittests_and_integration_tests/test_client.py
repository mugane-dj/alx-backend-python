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
        """
        Mock property org
        """
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock):
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "private": False,
                },
            ],
        }
        mock_get_json.return_value = test_payload["repos"]
        instance = GithubOrgClient("google")
        mock_public_repos_url = PropertyMock(
            return_value=test_payload["repos_url"]
        )
        with patch.object(
            instance.__class__, "_public_repos_url", mock_public_repos_url
        ):
            self.assertEqual(
                instance.public_repos(),
                [
                    "episodes.dart",
                    "cpp-netlib",
                ],
            )
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
