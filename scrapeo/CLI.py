"""The CLI Module
=============

This module provides classes and functions used in Scrapeo's command-
line interface to handle arguments passed to the program.
"""
### Notes ###
# query_key and query_val: {query_key: query_val}
# query_key and not query_val: {query_key: .*}
# not query_key and query_val: {search_val: query_val}


import re

class QueryBuilder(object):

    def __init__(self, config=None):
        self._queries = []
        self._collected_params = None
        self._config = config or {}

    def build_queries(self, params):
        # should return an iterator of built queries
        self._collected_params = params
        for param_set in self.collected_params:
            query = self.build_query(param_set)
            self._queries.append(query)
        return self._queries

    def build_query(self, param_set):
        query = self.__new_query()
        return query.build(param_set)

    @property
    def collected_params(self):
        return self.__group_params()

    @property
    def shortcuts(self):
        return self._config.get('shortcuts', {})

    @property
    def option_names(self):
        return self._config.get('option_names', [])

    def __new_query(self):
        return Query(config=self.option_names)

    def __group_params(self):
        # initialize list to collect all params
        grouped_params = []
        # add the option params to the list
        option_params = self.__get_params_from_options()
        grouped_params.extend(option_params)
        # add the shortcut params to the list
        shortcut_params = self.__get_params_from_shortcuts()
        grouped_params.extend(shortcut_params)
        return grouped_params

    def __get_params_from_options(self):
        option_params = []
        option_params.append({k: v for k, v in self._collected_params.items() if k in self.option_names})
        return option_params

    def __get_params_from_shortcuts(self):
        shortcut_params = []
        for shortcut, param_set in self.shortcuts.items():
            if self._collected_params.get(shortcut, False):
                shortcut_params.append(param_set)
        return shortcut_params

class Query(object):

    def __init__(self, config=None):
        self._config = config or []

    def build(self):
        pass
