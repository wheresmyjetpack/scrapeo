import argparse
import sys
import re
import requests.exceptions

# TODO add pretty text formatting

# Relative imports
from .core import Scrapeo, ElementAttributeError
from .utils import web_scraper

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

    ### process command-line arguments ###
    # meta subparser
    if args.command == 'meta':
        # defaults
        seo_attr = None
        search_val = None
        attrs = {}
        # --attr, --val
        if args.metatag_val or args.metatag_attr:
            # --seoattribute
            if args.seo_attr:
                seo_attr = args.seo_attr
            # --val only
            if args.metatag_val and not args.metatag_attr:
                search_val = args.metatag_val
            # --attr only
            elif args.metatag_attr and not args.metatag_val:
                attrs[args.metatag_attr] = re.compile('.*')
            # --attr and --val
            else:
                attrs[args.metatag_attr] = args.metatag_val

            try:
                # find and print the relevant text
                print(scrapeo.get_text('meta', search_val=search_val,
                                   seo_attr=seo_attr, **attrs))
            except ElementAttributeError as e:
                # element found, but missing attribute specified by '-s'
                print('The element returned by your search does not'
                      'contain the attribute "%s".' % e.attr)
                print(e.element)

        # --description
        if args.meta_description:
            print(scrapeo.get_text('meta', name='description'))

        # --title
        if args.title_tag:
            print(scrapeo.get_text('title'))

        # --robots
        if args.robots_meta:
            print(scrapeo.get_text('meta', name='robots'))

    # content subparser
    if args.command == 'content':
        # --heading 
        if args.heading_type:
            print(scrapeo.get_text(args.heading_type))
