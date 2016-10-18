Scrapeo
=======================

A command-line SEO web scraping / analysis tool

### Usage ###
1. Run `git clone git://github.com/wheresmyjetpack/scrapeo.git`


### Concept ###
* Scrape and analyze elements like meta data and content from web pages
* Provide a quick and easy-to-use tool for those who prefer command-line interfaces
* Generate reports on a web page's SEO "health"


### Features ###
* Installation via pip or make


### More commands ###
* **make test** - run all tests
* **make deb** - build Debian package (Incomplete)
* **make source** - build source tarball
* **make daily** - make daily snapshot
* **make install** - install program
* **make init** - install all requirements
* **make clean** - clean project, remove *.pyc and other temporary files
* **make deploy** - create vitrual environment


        |-- docs
        |   `-- doc.txt
        |-- scrapeo
        |   |-- data
        |   |   `-- some_data.html
        |   |-- utils
        |   |   |-- __init__.py
        |   |   |-- web_scraper.py
        |   |-- __init__.py
        |   |-- core.py
        |   |-- main.py
        |   |-- helpers.py
        |-- tests
        |   |-- __init__.py
        |   |-- test_helpers.py
        |   |-- test_Scrapeo.py
        |-- Makefile
        |-- CHANGES.txt
        |-- LICENSE.txt
        |-- README.md
        |-- requirements-dev.txt
        |-- requirements.txt
        `-- setup.py
