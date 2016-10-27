#!/usr/bin/env python

import unittest
import os
import re

from bs4 import BeautifulSoup
from unittest.mock import Mock
from scrapeo.core import Scrapeo
from tests.stubs import ElementStub

class ScrapeoTest(unittest.TestCase):

    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.html_file = os.path.join(tests_dir, 'data/document.html')

    # @unittest.skip('skipping')
    def test_sends_find_to_dom_parser(self):
        with open(self.html_file, 'r') as html:
            mocked_dom_parser = Mock()
            scrapeo = Scrapeo(html.read(), dom_parser=mocked_dom_parser)
            expected = {'search_val': 'Content-Type',
                           'content': 'text/html'}
            scrapeo.find_tag('meta', **expected)
            mocked_dom_parser.find.assert_called_with('meta', **expected)

    # @unittest.skip('skipping')
    def test_sends_relevant_text_to_analyzer(self):
        with open(self.html_file, 'r') as html:
            mocked_analyzer = Mock()
            scrapeo = Scrapeo(html.read(), analyzer=mocked_analyzer)
            expected_tag = ElementStub
            scrapeo.get_text(expected_tag, seo_attr='charset')
            mocked_analyzer.relevant_text.assert_called_with(expected_tag, seo_attr='charset')
