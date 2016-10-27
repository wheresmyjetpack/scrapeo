#!/usr/bin/env python

import unittest
import os
import re

from bs4 import BeautifulSoup
from unittest.mock import Mock
from scrapeo.core import Scrapeo

class ScrapeoTest(unittest.TestCase):

    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.html_file = os.path.join(tests_dir, 'data/document.html')
        self.kwargs = {'search_val': 'Content-Type',
                       'seo_attr': 'charset',
                       'content': 'text/html'}
        with open(self.html_file, 'r') as html:
            self.scrapeo = Scrapeo(html.read())

    def test_sends_find_to_dom_parser(self):
        with open(self.html_file, 'r') as html:
            mocked_dom_parser = Mock()
            scrapeo = Scrapeo(html.read(), dom_parser=mocked_dom_parser)
            expected = {k: v for k, v in self.kwargs.items() if not 'seo_attr' in k}
            scrapeo.get_text('meta', **self.kwargs)
            mocked_dom_parser.find.assert_called_with('meta', **expected)

    @unittest.skip('skipping')
    def test_sends_relevant_text_to_analyzer(self):
        """ .. todo:: Need to separate out the relevant text message send to a
            a seperate method for Scrapeo. Test currently too expensive
            to write.
        """
        with open(self.html_file, 'r') as html:
            mocked_analyzer = Mock()
            scrapeo = Scrapeo(html.read(), analyzer=mocked_analyzer)
            soup = BeautifulSoup('<meta charset="utf-8" content="text/html" http-equiv="Content-Type"/>', 'html5lib')
            expected_tag = soup.meta
            scrapeo.get_text('meta', **self.kwargs)
            mocked_analyzer.relevant_text.assert_called_with(expected_tag, seo_attr='charset')
