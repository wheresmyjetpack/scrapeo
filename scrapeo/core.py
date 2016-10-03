#!/usr/bin/env python

from bs4 import BeautifulSoup

class Scrapeo(object):

    def __init__(self, html, dom_parser=None):
        self.dom_parser = dom_parser or DomNavigator(html)

    """Public
    """
    def element_text(self, keyword, **kwargs):
        element = self.__find_tag(keyword, **kwargs)
        return self.__relevant_text(element)

    """Private
    """
    def __find_tag(self, keyword, **kwargs):
        return self.dom_parser.find(keyword, **kwargs)

    def __relevant_text(self, node):
        return node.relevant_text()


class DomNavigator(object):

    def __init__(self, html, parser=None):
        self.parser = parser or BeautifulSoup
        self.dom = self.__parse(html)

    """Public
    """
    def find(self, keyword, list_all=False, **kwargs):
        if list_all:
            return self.dom.find_all(keyword, attrs=kwargs)
        else:
            return HTMLElement(self.dom.find(keyword, attrs=kwargs))

    """Private
    """
    def __parse(self, html):
        return self.parser(html, 'html.parser')


class HTMLElement(object):

    def __init__(self, element):
        self.element = element

    """Public
    """
    def relevant_text(self):
        return self.__determine_seo_text()

    """Private
    """
    def __determine_seo_text(self):
        if self.__is_empty_element():
            return self.__meta_tag_content()
        return self.__node_text()

    def __node_text(self):
        return self.element.text

    def __meta_tag_content(self, attr=None):
        if attr:
            return self.element[attr]
        else:
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
