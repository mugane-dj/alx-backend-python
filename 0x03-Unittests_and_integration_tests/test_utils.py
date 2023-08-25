#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import Dict, Tuple, Union

access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test utils function access_nested_map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected_result: Union[Dict, int],
    ) -> None:
        """
        Tests access_nested_map returns output from mapping with provided sequence
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand(
        [({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)]
    )
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple[str], expected_result: Exception
    ) -> None:
        """
        Tests access_nested_map raises exception
        """
        if issubclass(expected_result, Exception):
            with self.assertRaises(expected_result):
                access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests for get_json function
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Tests get_json can be mocked successfully
        """
        mock_res = Mock()
        mock_res.json.return_value = test_payload

        with patch("requests.get") as mock_get:
            mock_get.return_value = mock_res
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
