#!/usr/bin/env python

import re
from bs4 import BeautifulSoup

class Scrapeo(object):

    def __init__(self, html, dom_parser=None):
        self.dom_parser = dom_parser or DomNavigator(html)

    """Public
    """
    def element_text(self, keyword, **kwargs):
        seo_attr = kwargs.pop('seo_attr', None)
        element = self.__find_tag(keyword, seo_attr=seo_attr, **kwargs)
        return self.__relevant_text(element)

    """Private
    """
    def __find_tag(self, keyword, seo_attr=None, **kwargs):
        return self.dom_parser.find(keyword, seo_attr=seo_attr, **kwargs)

    def __relevant_text(self, node):
        return node.relevant_text()


class DomNavigator(object):

    def __init__(self, html, parser=None):
        self.parser = parser or BeautifulSoup
        self.dom = self.__parse(html)

    """Public
    """
    def find(self, keyword, list_all=False, **kwargs):
        seo_attr = kwargs.pop('seo_attr', None)
        ele_attrs = kwargs
        if list_all:
            return self.dom.find_all(keyword, attrs=ele_attrs)
        else:
            return self.__search_for(keyword, search_attr=seo_attr, **ele_attrs)

    """Private
    """
    def __search_for(self, keyword, search_attr=None, **kwargs):
        if search_attr and not any(kwargs):
            # assume the tag contains only one attribute, which is the one we're interested in
            kwargs[search_attr] = re.compile('.*')
        return self.__html_element(self.dom.find(keyword, attrs=kwargs), search_attr)

    def __parse(self, html):
        return self.parser(html, 'html.parser')

    def __html_element(self, tag, seo_attr):
        return HTMLElement(tag, seo_attr)



class HTMLElement(object):
    """Wrapper for BeautifulSoup Tag
    Determines relevant SEO properties and attributes for a particular tag
    """

    def __init__(self, element, seo_attr=None):
        self.element = element
        self.seo_attr = seo_attr

    """Public
    """
    def relevant_text(self):
        return self.__determine_seo_text()

    """Private
    """
    def __determine_seo_text(self):
        if self.__is_empty_element():
            return self.__closed_tag_contents()
        return self.__node_text()

    def __node_text(self):
        return self.element.text

    def __closed_tag_contents(self):
        if self.seo_attr:
            # Return the text value of the relevant seo attribute
            return self.element[self.seo_attr]
        else:
            # Default is for the typical meta tag content attribute
            return self.element['content']

    def __is_empty_element(self):
        return self.element.is_empty_element


class WebScraper(object):

    def __init__(self, http_client):
        self.http_client = http_client

    """Public
    """
    def scrape(self, url):
        req = self.__http_get(url)
        return self.__document_from(req)

    """Private
    """
    def __http_get(self, url):
        return self.http_client.get(url)

    def __document_from(self, request):
        return request.text
