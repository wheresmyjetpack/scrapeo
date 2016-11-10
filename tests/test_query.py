import unittest

from scrapeo.CLI import Query

class QueryTest(unittest.TestCase):

    def setUp(self):
        self.options = {'metatag_attr': 'metatag_val'}
        self.shortcuts = {
                         'canonical': {
                             'element': 'link',
                             'rel': 'canonical',
                             'seo_attr': 'href'}
                         }
        self.query = Query(option_groups=self.options, shortcuts=self.shortcuts)

    def test_builds_from_options(self):
        expected = {'name': 'description'}
        self.assertEqual(expected, self.query.build({'metatag_attr': 'name', 'metatag_val': 'description'}))

    def test_builds_from_shortcuts(self):
        expected = self.shortcuts['canonical']
        self.assertEqual(expected, self.query.build({'canonical': True}))

    #@unittest.skip('skipping')
    def test_build_sets_value_to_wildcard_when_value_is_none(self):
        query = Query(option_groups=self.options, shortcuts=self.shortcuts, wildcard_val='wildcard')
        expected = {'name': 'wildcard'}
        self.assertEqual(expected, query.build({'metatag_attr': 'name'}))

    def test_build_sets_the_single_value_paramter_when_attr_is_none(self):
        expected = {'search_val': 'description'}
        self.assertEqual(expected, self.query.build({'metatag_val': 'description'}))
