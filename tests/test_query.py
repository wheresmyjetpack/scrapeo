import unittest

from scrapeo.CLI import Query

class QueryTest(unittest.TestCase):

    def setUp(self):
        self.conf = {'options': {'metatag_attr': 'metatag_val'},
                     'shortcuts': {
                         'canonical': {
                         'element': 'link',
                         'rel': 'canonical',
                         'seo_attr': 'href'}
                         }}

    def test_builds_from_options(self):
        query = Query(conf=self.conf)
        expected = {'name': 'description'}
        self.assertEqual(expected, query.build({'metatag_attr': 'name', 'metatag_val': 'description'}))

    def test_builds_from_shortcuts(self):
        query = Query(conf=self.conf)
        expected = self.conf['shortcuts']['canonical']
        self.assertEqual(expected, query.build({'canonical': True}))

    #@unittest.skip('skipping')
    def test_build_sets_value_to_wildcard_when_value_is_none(self):
        query = Query(conf=self.conf, wildcard_val='wildcard')
        expected = {'name': 'wildcard'}
        self.assertEqual(expected, query.build({'metatag_attr': 'name'}))

    def test_build_sets_the_single_value_paramter_when_attr_is_none(self):
        query = Query(conf=self.conf)
        expected = {'search_val': 'description'}
        self.assertEqual(expected, query.build({'metatag_val': 'description'}))
