"""Web scraping functions used by the Scrapeo module"""

import requests


def scrape(url):
    try:
        req = do_GET(url)
    except requests.exceptions.MissingSchema:
        url = 'http://' + url
        print('Rebuilding URL to %s\n' % url)
        req = do_GET(url)
    return document_from(req)

def do_GET(url):
    req = requests.get(url)
    req.raise_for_status
    return req

def document_from(request):
    return request.text
