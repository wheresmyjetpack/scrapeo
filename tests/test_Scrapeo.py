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

    def test_gets_value_from_seo_attr_when_specified(self):
        self.assertEqual('UTF-8', self.scrapeo.get_text('meta', seo_attr='charset', **{'http-equiv': 'Content-Type'}))

    def test_gets_value_from_content_when_no_seo_attr_specified(self):
        self.assertEqual('The description', self.scrapeo.get_text('meta', name='description'))

    def test_gets_content_from_first_tag_with_attr_value_when_no_attr_specified(self):
        self.assertEqual('noindex,nofollow', self.scrapeo.get_text('meta', search_val='robots'))
