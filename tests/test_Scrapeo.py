#!/usr/bin/env python

import unittest
import os

from scrapeo.core import Scrapeo

class ScrapeoTest(unittest.TestCase):

    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.html_file = os.path.join(tests_dir, 'data/document.html')
        #self.scrapeo = Scrapeo(open(self.html_file, 'r').read())
        with open(self.html_file, 'r') as html:
            self.scrapeo = Scrapeo(html.read())


    def test_gets_text_from_element(self):
        self.assertEqual('The title', self.scrapeo.element_text('title'))

    def test_gets_content_from_meta_tag(self):
        self.assertEqual('The description', self.scrapeo.element_text('meta', name='description'))
