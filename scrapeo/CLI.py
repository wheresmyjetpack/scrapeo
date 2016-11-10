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
    def shortcuts(self):
        return self._config.get('shortcuts', {})

    def __new_query(self):
        return Query(conf=self._config)

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
                shortcut_params.append({shortcut: self._collected_params[shortcut]})
        return shortcut_params


class Query(object):
    """Combines parameters into a set of key-value pairs usable by Scrapeo

    Query is used primarily to call `build` once to stitch together
    passed in parameters into a query dictionary. The query dict is
    constructed based on the `conf` passed into Query, as well as
    the `query_key` and `query_val` optional args.

    Note:
        The `conf` optional argument is a complex dictionary. It should
        at least have two keys, 'options' and 'shortcuts', each of
        which hold dictionaries as their values. 'options' are the
        names of keys that you will pass to `build`, with each pair
        of keys making a new key-value pair themselves.

        'shortcuts' have short, memorable strings as keys to pre-built
        queries. This allows you to pass in the shortcut key with a value
        of `True` to build the shortcut from the `conf`.

    Keyword Args:

    """

    def __init__(self, conf=None, query_key=None, query_val=None, wildcard_val=None):
        self.options = conf.get('options', {})
        self.shortcuts = conf.get('shortcuts', {})
        self.query_key = query_key or self.default_query_key
        self.query_val = query_val or self.default_query_val
        self._wildcard = wildcard_val or re.compile('.*')
        self._params = {}

    def build(self, params):
        query = {}
        try:
            first_key = list(params.keys())[0]
        except IndexError:
            pass
        else:
            if self.__is_shortcut(first_key):
                return self.shortcuts[first_key]
        return self.build_from_options(params)

    def build_from_options(self, params):
        param_key = params.pop(self.query_key, None)
        param_val = params.pop(self.query_val, None)
        self.__set_query_key_value(param_key, param_val)
        self._params.update(params)
        return self._params

    @property
    def default_query_key(self):
        try:
            return list(self.options.keys())[0]
        except IndexError:
            return None

    @property
    def default_query_val(self):
        try:
            return list(self.options.values())[0]
        except IndexError:
            return None

    def __set_query_key_value(self, key, val):
        if key is not None and val is not None:
            self._params[key] = val
        elif key is not None and val is None:
            self.__set_key_to_wildcard(key)
        elif key is None and val is not None:
            self.__set_single_value_param(val)

    def __set_key_to_wildcard(self, key):
        self._params[key] = self._wildcard

    def __set_single_value_param(self, val):
        self._params['search_val'] = val

    def __is_shortcut(self, key):
        return key in self.shortcuts.keys()
