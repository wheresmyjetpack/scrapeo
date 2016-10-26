#!/usr/bin/env python

import unittest
import os

from unittest.mock import patch, PropertyMock
from scrapeo.core import ElementAnalyzer

class ElementAnalyzerTest(unittest.TestCase):

    def setUp(self):
        self.element = ElementStub()
        self.analyzer = ElementAnalyzer()

    def test_gets_node_text_from_element_when_element_is_not_empty(self):
        self.assertEqual('text', self.analyzer.relevant_text(self.element))

    def test_gets_attributes_value_from_element_when_element_is_empty(self):
        with patch.object(ElementStub, 'is_empty_element', new_callable=PropertyMock) as mock:
            mock.return_value = True
            self.assertEqual('val', self.analyzer.relevant_text(self.element))


class ElementStub(object):

    attrs = {'attr': 'val'}
    is_empty_element = False
    text = 'text'

    def get(self, attr):
        return self.attrs.get('attr')
