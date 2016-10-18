#!/usr/bin/env python

import unittest
import os
import re

from scrapeo.core import Scrapeo

class ScrapeoTest(unittest.TestCase):

    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.html_file = os.path.join(tests_dir, 'data/document.html')
        #self.scrapeo = Scrapeo(open(self.html_file, 'r').read())
        with open(self.html_file, 'r') as html:
            self.scrapeo = Scrapeo(html.read())


    def test_gets_text_from_element(self):
        self.assertEqual('The title', self.scrapeo.get_text('title'))

    def test_gets_content_from_meta_tag(self):
        self.assertEqual('The description', self.scrapeo.get_text('meta', name='description'))

    def test_gets_canonical_href_from_link(self):
        self.assertEqual('http://example.com', self.scrapeo.get_text('link', seo_attr='href', rel='canonical'))

    def test_gets_meta_charset(self):
        self.assertEqual('UTF-8', self.scrapeo.get_text('meta', seo_attr='charset'))
