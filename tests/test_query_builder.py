import unittest

from unittest.mock import call, patch

from scrapeo.CLI import QueryBuilder, Query

class QueryBuilderTest(unittest.TestCase):

    def setUp(self):
        self.conf = {'options': {'metatag_val': 'metatag_attr'}, 'shortcuts': {'robots': {'name': 'robots'}}}
        self.query_builder = QueryBuilder(self.conf)

    #@unittest.skip('skipping')
    def test_groups_queries_based_on_config(self):
        params = {'metatag_attr': 'name', 'metatag_val': 'description', 'robots': True}
        with patch.object(Query, 'build') as mock_query_build:
            self.query_builder.build_queries(params)
            calls = [call({'metatag_attr': 'name', 'metatag_val': 'description'}),
                     call({'robots': True})]
            mock_query_build.assert_has_calls(calls)
