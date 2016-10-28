#!/usr/bin/env python

import unittest
import os
import re

from bs4 import BeautifulSoup
from unittest.mock import Mock, patch
from scrapeo.core import Scrapeo, ElementAnalyzer
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
            scrapeo = Scrapeo(html.read())
            with patch.object(ElementAnalyzer, 'relevant_text') as mock_relevant_text:
                scrapeo.get_text(ElementStub(), seo_attr='charset')
                mock_relevant_text.assert_called_with(seo_attr='charset')
