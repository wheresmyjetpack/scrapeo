"""Web scraping functions used by the Scrapeo module"""

import requests


def scrape(req):
    return document_from(req)

def do_GET(url):
    req = requests.get(url)
    req.raise_for_status
    return req

def document_from(request):
    return request.text
