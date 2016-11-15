"""The CLI Module
=============

This module provides classes and functions used in Scrapeo's command-
line interface to handle arguments passed to the program.
"""
### Notes ###


import re

class QueryBuilder(object):
    """Use a config to separate arbitrary params into individual queries.

    Note:
        The `config` optional argument is a complex dictionary. It should
        at least have two keys, 'options' and 'shortcuts', each of
        which hold dictionaries as their values. 'options' are the
        names of keys that you will pass to `build_queries`, with each pair
        of keys making a new key-value pair themselves.

        'shortcuts' have short, memorable strings as keys to pre-built
        queries. This allows you to pass in the shortcut key with a value
        of `True` to build the shortcut from the `config`.
    """

    def __init__(self, config=None):
        self._queries = []
        self._collected_params = None
        self._config = config or {}

    @property
    def collected_params(self):
        return self._group_params()

    @property
    def shortcuts(self):
        return self._config.get('shortcuts', {})

    @property
    def options(self):
        return self._config.get('options', {})

    ### Public ###
    def build_queries(self, params):
        # should return an iterator of built queries
        self._collected_params = params
        for param_set in self.collected_params:
            query = self.build_query(param_set)
            self._queries.append(query)
        return self._queries

    def build_query(self, param_set):
        query = self._new_query()
        return query.build(param_set)

    def _new_query(self):
        return Query(shortcuts=self.shortcuts, option_groups=self.options)

    def _group_params(self):
        # initialize list to collect all params
        grouped_params = []
        # add the option params to the list
        options = self._get_options()
        grouped_params.extend(options)
        # add the shortcut params to the list
        shortcuts = self._get_shortcuts()
        grouped_params.extend(shortcuts)
        return grouped_params

    def _get_options(self):
        # TODO this grabs the extra params (command, url) and builds a query out of them, which shouldn't be happening
        option_params = []
        blacklist = ['command', 'url']
        blacklist.extend(self.shortcuts.keys())
        option_params.append({k: v for k, v in self._collected_params.items() if k not in blacklist})
        return option_params

    def _get_shortcuts(self):
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

    Keyword Args:
        conf (dict): A multi-dimenional dict, containing 'options'
            groupings and pre-built queries as 'shortcuts'.
        query_key (str): Instead of a conf, a single value can be specfied
            to be used as a key in the params passed to `build`.
        query_val (str): A second key that will be passed to `build`,
            the value of this and `query_key` in the paramaters passed to `build`
            will be zipped together as a key-value pair in the returned query.

    """

    def __init__(self, shortcuts=None, option_groups=None, query_key=None, query_val=None, wildcard_val=None):
        self.options = option_groups or {}
        self.shortcuts = shortcuts or {}
        self.query_key = query_key or self.default_query_key
        self.query_val = query_val or self.default_query_val
        self._wildcard = wildcard_val or re.compile('.*')
        self._params = {}

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

    def build(self, params):
        query = {}
        try:
            first_key = list(params.keys())[0]
        except IndexError:
            pass
        else:
            if self._is_shortcut(first_key):
                return self.shortcuts[first_key]
        return self.build_from_options(params)

    def build_from_options(self, params):
        param_key = params.pop(self.query_key, None)
        param_val = params.pop(self.query_val, None)
        self._set_query_key_value(param_key, param_val)
        self._params.update(params)
        return self._params

    def _set_query_key_value(self, key, val):
        if key is not None and val is not None:
            self._params[key] = val
        elif key is not None and val is None:
            self._set_key_to_wildcard(key)
        elif key is None and val is not None:
            self._set_single_value_param(val)

    def _set_key_to_wildcard(self, key):
        self._params[key] = self._wildcard

    def _set_single_value_param(self, val):
        self._params['search_val'] = val

    def _is_shortcut(self, key):
        return key in self.shortcuts.keys()
