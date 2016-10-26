#!/usr/bin/env python

import unittest
import os

from scrapeo.core import DomNavigator

class DomNavigatorTest(unittest.TestCase):

    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.html_file = os.path.join(tests_dir, 'data/document.html')
        with open(self.html_file, 'r') as html:
            self.dom_navigator = DomNavigator(html.read())
        self.tag = self.dom_navigator.find('meta', name='description')

    def test_finds_tag_using_specified_attribute_and_value(self):
        self.assertEqual('<meta content="The description" name="description"/>', str(self.tag))

    def test_finds_tag_using_single_value(self):
        self.assertEqual('<meta content="The description" name="description"/>', str(self.tag))
