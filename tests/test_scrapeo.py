#!/usr/bin/env python

import unittest
import os
import re

from unittest.mock import Mock
from scrapeo.core import Scrapeo

class ScrapeoTest(unittest.TestCase):

    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.html_file = os.path.join(tests_dir, 'data/document.html')
        with open(self.html_file, 'r') as html:
            self.scrapeo = Scrapeo(html.read())

    def test_sends_find_to_dom_parser(self):
        with open(self.html_file, 'r') as html:
            mocked_dom_parser = Mock()
            scrapeo = Scrapeo(html.read(), dom_parser=mocked_dom_parser)
            kwargs = {'search_val': 'description', 'seo_attr': 'content',
                      'name': 'og:description'}
            expected = {k: v for k, v in kwargs.items() if not 'seo_attr' in k}
            scrapeo.get_text('meta', **kwargs)
            mocked_dom_parser.find.assert_called_with('meta', **expected)

    def test_gets_value_from_seo_attr_when_specified(self):
        self.assertEqual('UTF-8', self.scrapeo.get_text('meta',
                         seo_attr='charset',
                         **{'http-equiv': 'Content-Type'}))

    def test_gets_value_from_content_when_no_seo_attr_specified(self):
        self.assertEqual('The description', self.scrapeo.get_text('meta', name='description'))

    def test_gets_content_from_first_tag_with_attr_value_when_no_attr_specified(self):
        self.assertEqual('noindex,nofollow', self.scrapeo.get_text('meta', search_val='robots'))
