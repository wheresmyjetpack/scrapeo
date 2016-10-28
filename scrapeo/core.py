"""Core Classes for the Scrapeo Package
=====================================

This module contains classes used to parse and handle HTML as a Python
object, search by combinations of element attribute and value pairs,
and scrape node and attribute value text from nodes.
"""

from bs4 import BeautifulSoup

import scrapeo.exceptions as exceptions
from .helpers import pop_kwargs

class Scrapeo(object):
    """Parse HTML into an object, search and get relevant element text.

    Facilitates searching and scraping functionality for appropriately
    parsed HTML.

    Args:
        html (str): string, HTML in text format

    Keyword Args:
        dom_parser (obj): an object that responds to the `find` message
        analyzer (type): a class name which, when instantiated, responds
            to the `relevant_text` message
    """
    def __init__(self, html, dom_parser=None, analyzer=None):
        self.dom_parser = dom_parser or self.__default_dom_parser()(html)
        self.analyzer = analyzer or ElementAnalyzer

    ### Public ###
    def find_tag(self, search_term, **kwargs):
        """Find a specific tag from an HTML document.

        Search a document using an element name, attribute-value pairs,
        or using a single value. Scrapeo will ignore a value assigned
        to `search_val` if there are any attribute-value pairs provided
        as keyword arguments.

        Args:
            search_term (str): name of an HTML element

        Keyword Args:
            search_val (str): for a tag to be returned as a result, one
                of its attributes must have this value. Used to search
                tags by value instead of attribute-value pairs.
            **kwargs: arbitrary element attribute-value pairs to search
                for

        Returns:
            obj: An object representing a HTML element, which minimally
            provides a `text` attribute and a `get` dict-like method.
        """
        return self.__dom_search(search_term, **kwargs)

    def get_text(self, element, seo_attr=None):
        """Get text from an HTML tag.

        Retrieve arbitrary text from an object representing an HTML
        element by making a call to `self.analyzer`.

        Args:
            element (obj): the object representing the HTML element

        Keyword Args:
            seo_attr (str): optionally specify an attribute of the
                element to scrape a value from

        Returns:
            str: The text from an element, which is either the node
                text or some attribute's value.
        """
        return self.__relevant_text(element, seo_attr=seo_attr)

    ### Private ###
    def __dom_search(self, search_term, **kwargs):
        return self.dom_parser.find(search_term, **kwargs)

    def __relevant_text(self, element, seo_attr=None):
        analyzer = self.analyzer(element)
        return analyzer.relevant_text(seo_attr=seo_attr)

    def __default_dom_parser(self):
        return DomNavigator


class DomNavigator(object):
    """Navigate HTML by searching for names, attributes, and values.

    Parses HTML in text format into an object suitable for searching.
    Provides a method to search the parsed HTML for an element name,
    an attribute-value pair, or simply by a value held by an arbirary
    attribute.

    .. todo:: DomNavigator should become WebScraper, and we're going to pass
        a URL to Scrapeo instead of HTML as a string. The WebScraper will
        do the work of making an HTTP request and retrieving the document.

    Args:
        html (str): any portion of HTML text

    Keyword Args:
        parser (obj): the object used to do the parsing
        parser_type (str): the type of python parser used by the parser
            object
    """
    def __init__(self, html, parser=None, parser_type='html5lib'):
        self.parser = parser or self.__default_parser()
        self.dom = self.__parse(html, parser_type)

    ### Public ###
    def find(self, search_term, search_val=None, **kwargs):
        """Find and return an HTML element using provided search terms.

        Args:
            search_term (str): search for elements by name

        Keyword Args:
            search_val (str): search for an element with an attribute
                value matching search_val
            **kwargs: arbitrary element attr-val pairs

        Returns:
            obj: HTML element as a python object

        Raises:
            ElementNotFoundError: When no element can be found using
                the search terms
        """
        ele_attrs = kwargs
        return self.__get_tag(search_term, search_val, **ele_attrs)

    ### Private ###
    def __get_tag(self, keyword, search_val, **kwargs):
        if search_val and not any(kwargs):
            tag = self.__search_by_value(keyword, search_val)
        else:
            tag = self.__search(keyword, **kwargs)

        if tag is None:
            exceptions.raise_element_not_found_error(search_term=keyword,
                                                     value=search_val,
                                                     attrs=kwargs)
            return
        return tag

    def __search(self, keyword, **kwargs):
        return self.dom.find(keyword, attrs=kwargs)

    def __search_by_value(self, keyword, value):
        for tag in self.dom.find_all(keyword):
            if value in tag.attrs.values():
                return tag

    def __parse(self, html, parser_type):
        return self.parser(html, parser_type)

    def __default_parser(self):
        return BeautifulSoup


class ElementAnalyzer(object):
    """Get text from an HTML element.

    Determines what useful or relevant text an HTML element contains
    and returns it as a string. Takes an object that represents an
    HTML element as a positional argument.

    Args:
        element (obj): an object that responds to messages for the
            `text` (str) and `is_empty_element` (bool) attributes,
            and has a dict-like `get` method
    """
    def __init__(self, element):
        self.element = element

    ### Public ###
    def relevant_text(self, seo_attr=None):
        """Get pertinent text from an HTML element.

        Given an element's type and (optionally) a particular attribute,
        retrieve text from the element. Text could either be the text
        content of the node or the value of a particular attribute.

        Keyword Args:
            seo_attr (str): attribute of element to retrieve a value
                from

        Returns:
            str: node text if self.element is empty / self-closing or
            if seo_attr is not None; the value of an attribute
            as text otherwise

        Raises:
            ElementAttributeError: If seo_attr is not an attribute of
                element
        """
        if self.__is_empty_element() or seo_attr is not None:
            return self.__value_from_attr(seo_attr)
        return self.__node_text()

    ### Private ###
    def __value_from_attr(self, seo_attr):
        attr = 'content'
        if seo_attr is not None:
            # Overwrite the value of the relevant attribute
            attr = seo_attr
        val = self.element.get(attr)

        if val is None:
            exceptions.raise_element_attribute_error(element=self.element,
                                                     attr=attr)
        else:
            return val

    def __node_text(self):
        return self.element.text

    def __is_empty_element(self):
        return self.element.is_empty_element
