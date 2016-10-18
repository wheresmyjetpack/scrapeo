import argparse
import sys

from .core import Scrapeo, DomNavigator, SEOAnalyzer
from .utils import web_scraper

def main():
    argparser = argparse.ArgumentParser(
        prog='scrapeo',
        description='A command-line web scraper and SEO analysis tool')

    subparsers = argparser.add_subparsers(help='sub-command help')

    # content sub-command
    parser_content = subparsers.add_parser('content',
                                           help='content help')
    parser_content.add_argument('-H', '--heading', nargs='?',
                                dest='heading_type', const='h1')

    # meta sub-command
    parser_meta = subparsers.add_parser('meta', help='meta help')
    # options
    parser_meta.add_argument('-a', '--attr',
                             nargs='?', metavar='attribute',
                             dest='metatag_attr', const='name',
                             default='name')
    parser_meta.add_argument('-v', '--val', nargs='?', metavar='value',
                             dest='metatag_val', const='description',
                             default=argparse.SUPPRESS)
    # flags
    parser_meta.add_argument('-t', '--title', dest='title_tag',
                             action='store_true')
    parser_meta.add_argument('-d', '--description',
                             dest='meta_description', action='store_true')

    # URL positional argument
    argparser.add_argument('url')
    args = argparser.parse_args()
    # DEBUG
    print(args)

    html = web_scraper.WebScraper().scrape(args.url)
    scrapeo = Scrapeo(html)

    if args.metatag_val or args.metatag_attr != 'name':
        print(scrapeo.get_text(
            'meta', **{args.metatag_attr: args.metatag_val}))

    if args.title_tag:
        print(scrapeo.get_text('title'))
