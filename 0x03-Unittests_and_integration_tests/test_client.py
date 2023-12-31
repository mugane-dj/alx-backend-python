#!/usr/bin/env python3
"""
Tests on TestGithubOrgClient class methods and properties
"""

import unittest
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from typing import Dict, Union
from requests.exceptions import HTTPError
from parameterized import parameterized, parameterized_class

GithubOrgClient = __import__("client").GithubOrgClient
TEST_PAYLOAD = __import__("fixtures").TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests on GithubOrgClient methods
    """

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("holberton", {"login": "holberton"}),
        ]
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

    def test_public_repos_url(self) -> None:
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
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test public_repos func
        """
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

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(
        self, repo: Dict[str, Dict], license_key: str, expected_result: bool
    ) -> None:
        """
        Test has_license static method
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected_result
        )


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        }
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient.public_repos
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Setup fixtures
        """
        payloads = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def load_payload(url: str) -> Union[Mock, Exception]:
            if url in payloads:
                return Mock(**{"json.return_value": payloads[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=load_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """
        Test expected repos are returned
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(), self.expected_repos
        )

    def test_public_repos_with_license(self):
        """
        Test expected repos with Apache-2.0 license returned
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos("apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Teardown class method
        """
        cls.get_patcher.stop()
