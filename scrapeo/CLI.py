"""The CLI Module
=============

This module provides classes and functions used in Scrapeo's command-
line interface to handle arguments passed to the program.
"""

import re

class QueryBuilder(object):
    """A class for sorting paramaters into dict-type queries

    Given a dictionary containing they keys `metatag_attr` and
    `metatag_val`, build queries that are suitable to pass to Scrapeo
    for the purpose of searching the DOM.

    Args:
        collected_params (dict): Dictionary containing (at the very
            least) `metatag_attr` and `metatag_val` keys. Used to build
            custom queries. May also contain keys with boolean values
            whose names match up with `config` dictionary keys.

    Keyword Args:
        config (dict): A dictionary defining "shortcut" queries which
            can be referenced by their keys in the
            `prepare_shortcut_queries` public method.
    """

    def __init__(self, collected_params, config=None):
        self.collected_params = collected_params
        self.queries = []
        self.shortcuts = config or {}

    ### Public ###
    def prepare_queries(self):
        """Set the object's state so that it holds all parsed queries"""
        self.prepare_options_queries()
        self.prepare_shortcut_queries()

    def prepare_options_queries(self, element='meta'):
        """Handle key-value pair combinations"""
        if self.__has_param('metatag_attr') or self.__has_param('metatag_val'):
            search_params = {}
            search_params['search_val'] = self.__set_search_val()
            metatag_attr = self.collected_params['metatag_attr']
            search_params[metatag_attr] = self.__set_attr_val()
            search_params['element'] = element
            self.queries.append(search_params)

    def prepare_shortcut_queries(self):
        """Handle shortcuts for queries in the form of True/False flags"""
        for shortcut_name, shortcut in self.shortcuts.items():
            if self.collected_params.get(shortcut_name, False):
                self.queries.append(shortcut)

    ### Private ###
    def __set_search_val(self):
        # is there a meta value but no attribute?
        if self.__has_param('metatag_val') and not self.__has_param('metatag_attr'):
            # return value stored in the 'metatag_val' key
            return self.collected_params['metatag_val']
        # explicitly returning None if condition not met
        return None

    def __set_attr_val(self):
        # is there a meta attribute but no value?
        if self.__has_param('metatag_attr') and not self.__has_param('metatag_val'):
            # value can be anything
            return re.compile('.*')
        # or the value will just be whatever is stored
        return self.collected_params['metatag_val']

    def __has_param(self, param):
        return self.collected_params.get(param) is not None
