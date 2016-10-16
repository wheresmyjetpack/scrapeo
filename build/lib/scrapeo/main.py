import argparse
import sys

from .core import Scrapeo, DomNavigator, SEOAnalyzer
from .utils import web_scraper

def main():
    # intitialize the group_default variable
    group_default = None
    if len(sys.argv[1:]) > 1:
        # supress defaults if any options provided
        group_default = argparse.SUPPRESS

    argparser = argparse.ArgumentParser(
        prog='scrapeo',
        description='A command-line web scraper and SEO analysis tool'
    )

    subparsers = argparser.add_subparsers(help='sub-command help')

    # content sub-command
    parser_content = subparsers.add_parser('content', help='content help')
    parser_content.add_argument('-H', '--heading', nargs='?', dest='heading_type', const='h1')

    # meta sub-command
    # determine defaults
    meta_default = group_default or 'name:description'
    title_default = group_default or True

    parser_meta = subparsers.add_parser('meta', help='meta help')
    parser_meta.add_argument('-a', '--attr',
            nargs='?', metavar='attribute', dest='metatag_attr', const='name', default=meta_default)
    parser_meta.add_argument('-v', '--val',
            nargs='?', metavar='value', dest='metatag_val', const='description', default=meta_default)
    parser_meta.add_argument('-t', '--title',
            dest='title_tag', action='store_true', default=title_default)

    # URL positional argument
    argparser.add_argument('url')
    args = argparser.parse_args()
    #print(args)

    html = web_scraper.WebScraper().scrape(args.url)
    scrapeo = Scrapeo(html)
    print(scrapeo.seo_text('meta', **{args.metatag_attr: args.metatag_val}))
