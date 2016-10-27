#!/usr/bin/env python

import unittest
import os

from unittest.mock import patch, PropertyMock
from scrapeo.core import ElementAnalyzer
from tests.stubs import ElementStub

class ElementAnalyzerTest(unittest.TestCase):

    def setUp(self):
        self.element = ElementStub()
        self.analyzer = ElementAnalyzer()

    def test_gets_node_text_from_element_when_element_is_not_empty(self):
        self.assertEqual('text', self.analyzer.relevant_text(self.element))

    def test_gets_value_of_content_from_element_when_element_is_empty(self):
        element = ElementStub()
        element.is_empty_element = True
        self.assertEqual('val', self.analyzer.relevant_text(element))

    def test_gets_attribute_value_from_element_when_seo_attr_specified(self):
        expected = 'seo'
        actual = self.analyzer.relevant_text(self.element, seo_attr='property')
        self.assertEqual(expected, actual)


