"""The CLI Module
=============

This module provides classes and functions used in Scrapeo's command-
line interface to handle arguments passed to the program.
"""

import re

class QueryBuilder(object):
    """A class for sorting paramaters into dict-type queries"""

    def __init__(self, collected_params, config=None):
        self.collected_params = collected_params
        self.queries = []
        self.shortcuts = config or {}

    ### Public ###
    def prepare_queries(self):
        """Set the object's state so that it holds all parsed queries"""
        self.prepare_options_queries()
        self.prepare_shortcut_queries()

    def prepare_options_queries(self):
        """Handle key-value pair combinations"""
        if self.__has_param('metatag_attr') or self.__has_param('metatag_val'):
            element = 'meta'
            # --attr, --val
            search_params = {}
            # --val only
            search_params['search_val'] = self.__set_search_val()
            # --attr only
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
        if self.__has_param('metatag_val') and not self.__has_param('metatag_attr'):
            return self.collected_params['metatag_val']
        return None

    def __set_attr_val(self):
        if self.__has_param('metatag_attr') and not self.__has_param('metatag_val'):
            return re.compile('.*')
        return self.collected_params['metatag_val']

    def __has_param(self, param):
        return self.collected_params.get(param) is not None
