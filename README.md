Scrapeo
=======================

A command-line SEO web scraping / analysis tool

### Installation ###
1. Run `git clone git://github.com/wheresmyjetpack/scrapeo.git`
2. `cd` into the scrapeo directory and run `make deploy` to install required packages into a virtualenv
3. *Optional* (With super user privileges) `ln -s $HOME/.virtualenvs/venv/bin/scrapeo /usr/local/bin/scrapeo` (Or somehwere in your path)


### Concept ###
* Scrape and analyze elements like meta data and content from web pages
* Provide a quick and easy-to-use tool for those who prefer command-line interfaces
* Generate reports on a web page's SEO "health"


### Features ###
* Installation via pip or make
* Scrape meta description, page title, content from robots meta tag, and page headings
* Attempt to find meta tags by attr=val and scrape text from the value of one of its attributes


### Make commands ###
All of these are a work-in-progress, and many may end up being removed


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


### Changelog ###
#### 0.1.1.a1 ####
* Change make deploy virtualenv directory location
* Added `-s` CLI option for specifiying what element attribute to scrape a value from
* Improved and better named tests


#### 0.1.1.dev1 ####
* Unnecessary relative imports removed from CLI script
* Flag for scraping the content attribute of a robots meta tag
* Option for scraping the text from the first heading by type (h1,h2,h3,etc.)


#### 0.1.0 ####
* Initial development release
