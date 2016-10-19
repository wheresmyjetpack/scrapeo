#!/usr/bin/env python
# coding=utf-8

import unittest

from scrapeo.helpers import node_text

class ElementStub(object):

    def __init__(self):
        self.text = 'text'


class HelpersTest(unittest.TestCase):

    def test_node_text(self):
        element = ElementStub()
        self.assertEqual('text', node_text(element))


if __name__ == "__main__":
    unittest.main()
