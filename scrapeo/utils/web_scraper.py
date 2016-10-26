"""Utils for the Scrapeo package

.. todo:: This needs to be a set of module-level functions, and is not
    really a web scraper, but just a set of high level functions for
    making HTTP requests.
"""

import requests

class WebScraper(object):

    def __init__(self, http_client=None):
        self.http_client = http_client or self.__default_http_client()

    ### Public ###
    def scrape(self, url):
        req = self.__http_get(url)
        req.raise_for_status()
        return self.__document_from(req)

    ### Private ###
    def __http_get(self, url):
        return self.http_client.get(url)

    def __document_from(self, request):
        return request.text

    def __default_http_client(self):
        return requests
