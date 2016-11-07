"""Application code for the Scrapeo command-line client."""
# Python 2 compatibility
from __future__ import print_function

import argparse
import json
import os
import sys

import requests.exceptions

# Relative imports
from .core import Scrapeo
from .CLI import QueryBuilder
from .exceptions import ElementNotFoundError, ElementAttributeError
from .utils import web_scraper

PARENT_DIR = os.path.dirname(__file__)
SHORTCUTS_CONFIG_FILE = os.path.join(PARENT_DIR, 'shortcuts.conf')
with open(SHORTCUTS_CONFIG_FILE, 'r') as fh:
    SHORTCUTS_CONFIG = json.load(fh)

# TODO add pretty text formatting
# TODO add option to check what HTML spec a site makes use of

def main():
    """Main function for scrapeo CLI."""

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
    args = argparser.parse_args()
    url = args.url
    try:
        html = web_scraper.scrape(url)    # TODO need a try-except here
    except requests.exceptions.ConnectionError as e:
        print(e)
        sys.exit(1)
    # initialize scrapeo
    scrapeo = Scrapeo(html)
    # initialize a QueryBuilder to sort search parameters
    query_builder = QueryBuilder(vars(args), config=SHORTCUTS_CONFIG)
    query_builder.prepare_queries()

    if any(query_builder.queries):
        for query in query_builder.queries:
            # search for tag using paramters from query
            search_params = {k: v for k, v in query.items() if not k == 'seo_attr'}
            try:
                result = scrapeo.find_tag(**search_params)

            except ElementNotFoundError as e:
                print('No elements found.: %s' % vars(e))

            else:
                # found a tag
                # get the desired text from the found element
                seo_attr = query.get('seo_attr')
                try:
                    print(scrapeo.get_text(result,
                                           seo_attr=seo_attr))

                except ElementAttributeError as e:
                    # element found, but missing attribute specified by '-s'
                    print('The element returned by your search does not '
                          'contain the attribute "%s": %s' % (e.attr,
                                                              e.element))

        sys.exit(0)
