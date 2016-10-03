#!/usr/bin/env python

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
