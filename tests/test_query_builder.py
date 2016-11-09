import unittest

from scrapeo.CLI import QueryBuilder

class QueryBuilderTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_sorts_option_arguments_into_queries(self):
        params = {'metatag_attr': 'name', 'metatag_val': 'description'}
        query_builder = QueryBuilder(params)
        self.assertEqual([{'name': 'description', 'element': 'meta', 'search_val': None, 'seo_attr': None}], query_builder.prepare_queries())

    def test_sorts_shortcuts_into_queries(self):
        params = {'robots_meta': True}
        config = {'robots_meta': {'element': 'meta', 'name': 'robots'}}
        query_builder = QueryBuilder(params, config=config)
        self.assertEqual([{'element': 'meta', 'name': 'robots'}], query_builder.prepare_queries())

    def test_sets_query_search_val(self):
        params = {'metatag_attr': None, 'metatag_val': 'description'}
        query_builder = QueryBuilder(params)
        self.assertEqual([{'element': 'meta', 'search_val': 'description', 'seo_attr': None}], query_builder.prepare_queries())
