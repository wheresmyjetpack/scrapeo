#!/usr/bin/env python
# coding=utf-8

import unittest

from scrapeo.helpers import pop_kwargs

class PopKwargsTest(unittest.TestCase):

    def setUp(self):
        self.kwargs = {1: 'f', 2: 'o', 3: 'o'}

    def test_returns_values_for_keys(self):
        f, o, o = pop_kwargs(self.kwargs, 1, 2, 3)
        self.assertEqual(('f','o','o'), (f, o, o))

    def test_removes_key_value_pairs(self):
        f, o, o = pop_kwargs(self.kwargs, 1, 2, 3)
        self.assertEqual(self.kwargs, {})

if __name__ == "__main__":
    unittest.main()
