"""The CLI Module
=============

This module provides classes and functions used in Scrapeo's command-
line interface to handle arguments passed to the program.
"""
### Notes ###


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
    def options(self):
        return self._config.get('options', {})

    @property
    def shortcuts(self):
        return self._config.get('shortcuts', {})

    def __new_query(self):
        query_key, query_val = self.options.items()[0]
        return Query(conf=self.shortcuts, query_key=query_key,
                     query_val=query_val)

    def __group_params(self):
        # initialize list to collect all params
        grouped_params = []
        # add the option params to the list
        options = self.__get_options()
        grouped_params.extend(options)
        # add the shortcut params to the list
        shortcuts = self.__get_shortcuts()
        grouped_params.extend(shortcuts)
        return grouped_params

    def __get_options(self):
        option_params = []
        option_params.append({k: v for k, v in self._collected_params.items() if k not in self.shortcuts.keys()})
        return option_params

    def __get_shortcuts(self):
        shortcut_params = []
        for shortcut in self.shortcuts.keys():
            if self._collected_params.get(shortcut, False):
                shortcut_params.append({shorcut: self._collected_params[shortcut]})
        return shortcut_params

class Query(object):

    def __init__(self, conf=None, query_key='', query_val=''):
        self.conf = conf or {}
        self.query_key = query_key
        self.query_val = query_val
        self._params = None

    def build(self, params):
        query = {}
        first_key = params.keys()[0]
        if self.__is_shortcut(first_key):
            return self.conf[first_key]
        else:
            return self.build_from_options(params)

    def build_from_options(self, params):
        param_key = params.pop(self.query_key)
        param_val = params.pop(self.query_val)
        self._params[query_key] = query_val
        self.__set_query_key_value(param_key, param_val)
        self._params.update(params)
        return self._params

    def __set_query_key_value(self, key, val):
        # query_key and query_val: {query_key: query_val}
        # query_key and not query_val: {query_key: .*}
        # not query_key and query_val: {search_val: query_val}
        if key is not None and val is not None:
            return
        elif key is not None and val is None:
            self.__set_key_to_wildcard(key)
            return
        elif key is None and val is not None:
            self.__set_single_value_param(val)
        del self._params[key]

    def __set_key_to_wildcard(self, key):
        self._params[key] = re.compile('.*')

    def __set_single_value_param(self, val):
        self._params['search_val'] = self._params[val]

    def __is_shortcut(self, key):
        return key in self.conf.keys()
