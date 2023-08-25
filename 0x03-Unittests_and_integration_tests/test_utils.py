#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test utils function access_nested_map
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_result):
        if issubclass(expected_result, Exception):
            with self.assertRaises(expected_result):
                access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests for get_json function
    """

    @unittest.mock.patch('utils.requests.get')
    def test_get_json(self, mock_get):
        mock_res = unittest.mock.Mock()
        mock_res.json.return_value = {'data': 'mock_res'}
        mock_get.return_value = mock_res

        res = get_json('http://api.example.com/')

        self.assertEqual(res, {'data': 'mock_res'})
        mock_get.assert_called_once_with('http://api.example.com/')


# class TestClass:

#     def a_method(self):
#         """
#         A dummy method
#         """
#         return 42

#     @memoize
#     def a_property(self):
#         """
#         A memoized property should only call the method once
#         """
#         return self.a_method()

#     @unittest.mock.patch('utils.cache', {})
#     def test_memoize(self):
#         """
#         Test memoization
#         """
#         for _ in range(2):
#             result = self.a_property()

#         self.assertEquals(self.a_method(), result)
#         self.a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
