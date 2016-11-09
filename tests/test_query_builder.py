import unittest

from unittest.mock import Mock, patch

from scrapeo.CLI import QueryBuilder, Query

class QueryBuilderTest(unittest.TestCase):

    def setUp(self):
        self.conf = {'option_names': ['metatag_val', 'metatag_attr', 'seo_attr'], 'shortcuts': {'robots': {'name': 'robots'}}}
        self.query_builder = QueryBuilder(self.conf)

    @unittest.skip('skipping')
    def test_groups_queries_based_on_config(self):
        params = {'metatag_attr': 'name', 'metatag_val': 'description', 'robots': True}
        with patch.object(Query, 'build') as mock_query_build:
            self.query_builder.build_queries(params)
            #calls = [call('metatag_attr': 'name')]

    @unittest.skip('skipping')
    def test_sorts_shortcuts_into_queries(self):
        params = {'robots_meta': True}

    @unittest.skip('skipping')
    def test_sets_query_search_val(self):
        params = {'metatag_attr': None, 'metatag_val': 'description'}
