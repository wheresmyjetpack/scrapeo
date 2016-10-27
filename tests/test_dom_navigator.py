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

    def test_finds_tag_using_element_name(self):
        tag = self.dom_navigator.find('title')
        self.assertEqual('<title>The title</title>', str(tag))

    def test_finds_tag_using_specified_attribute_and_value(self):
        tag = self.dom_navigator.find('meta', name='description')
        self.assertEqual('<meta content="The description" name="description"/>', str(tag))

    def test_finds_tag_using_single_value(self):
        tag = self.dom_navigator.find('meta', search_val='robots')
        self.assertEqual('<meta content="noindex,nofollow" name="robots"/>', str(tag))
