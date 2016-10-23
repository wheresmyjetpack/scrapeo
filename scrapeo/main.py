# conditional python 2 import
from __future__ import print_function

import argparse
import re
import sys

import requests.exceptions

# Relative imports
from .core import Scrapeo, ElementAttributeError, ElementNotFoundError
from .utils import web_scraper

# TODO add pretty text formatting

argparser = argparse.ArgumentParser(
    prog='scrapeo',
    description='A command-line web scraper and SEO analysis tool')

# add sub-parsers
subparsers = argparser.add_subparsers(help='sub-command help',
                                      dest='command')

### content sub-command ###
parser_content = subparsers.add_parser('content',
                                       help='content help')
# options
parser_content.add_argument('-H', '--heading', nargs='?',
                            dest='heading_type', const='h1')

### meta sub-command ###
parser_meta = subparsers.add_parser('meta', help='meta help')
# options
parser_meta.add_argument('-a', '--attr',
                         nargs='?', metavar='attribute',
                         dest='metatag_attr', const='name')
parser_meta.add_argument('-v', '--val', metavar='value',
                         dest='metatag_val')
parser_meta.add_argument('-s', '--seoattribute', nargs='?',
                         metavar='relevant_attribute', dest='seo_attr')
# flags
parser_meta.add_argument('-t', '--title', dest='title_tag',
                         action='store_true')
parser_meta.add_argument('-d', '--description',
                         dest='meta_description',
                         action='store_true')
parser_meta.add_argument('-r', '--robots', dest='robots_meta',
                         action='store_true')
parser_meta.add_argument('-c', '--canonical', action='store_true')

# TODO add a flag to turn off text output formatting
# URL positional argument
argparser.add_argument('url')

def main():
    args = argparser.parse_args()
    # DEBUG
    #print(args)

    url = args.url
    # if the URL is missing the HTTP schema, add it
    try:
        html = web_scraper.WebScraper().scrape(url)
    except requests.exceptions.MissingSchema:
        url = 'http://' + url
        print('Rebuilding URL to %s\n' % url)
        html = web_scraper.WebScraper().scrape(url)

    # initialize scrapeo
    scrapeo = Scrapeo(html)
    # initialize list used to store each set of search params
    searches = []

    ### process command-line arguments ###
    # meta subparser
    if args.command == 'meta':
        # default element is a meta tag
        element = 'meta'
        # --attr, --val
        if args.metatag_val or args.metatag_attr:
            kwargs = {}
            # --seoattribute
            if args.seo_attr:
                kwargs['seo_attr'] = args.seo_attr
            # --val only
            if args.metatag_val and not args.metatag_attr:
                kwargs['search_val'] = args.metatag_val
            # --attr only
            elif args.metatag_attr and not args.metatag_val:
                kwargs[args.metatag_attr] = re.compile('.*')
            # --attr and --val
            else:
                kwargs[args.metatag_attr] = args.metatag_val
            searches.append([element, kwargs])

        # --description
        if args.meta_description:
            searches.append([element, {'name': 'description'}])

        # --robots
        if args.robots_meta:
            searches.append([element, {'name': 'robots'}])

        # --title
        if args.title_tag:
            element = 'title'
            searches.append([element, {}])

        # --canonical
        if args.canonical:
            element = 'link'
            searches.append([element, {'rel': 'canonical',
                                       'seo_attr': 'href'}])

    # content subparser
    if args.command == 'content':
        # --heading 
        if args.heading_type:
            element = args.heading_type
            searches.append([element, {}])

    search = lambda s: print(scrapeo.get_text(s[0], **s[1]))

    for query in searches:
        try:
            # find and print the relevant text
            search(query)

        except ElementAttributeError as e:
            # element found, but missing attribute specified by '-s'
            print('The element returned by your search does not '
                  'contain the attribute "%s".' % e.attr)
            print(e.element)

        except ElementNotFoundError as e:
            print('No elements found.')
            print(vars(e))

    sys.exit(0)
