Scrapeo
=======================

A command-line SEO web scraping / analysis tool

### Installation ###
1. Run `git clone git://github.com/wheresmyjetpack/scrapeo.git`
2. `cd` into the scrapeo directory and run `make deploy` to install required packages into a virtualenv
3. *Optional* (With super user privileges) `ln -s $HOME/.virtualenvs/venv/bin/scrapeo /usr/local/bin/scrapeo` (Or somehwere in your path)


*Alternative* -- Install via `pip`
* If installing in a virtualenv, simply run `pip install scrapeo`
* If installing to your global site-package directory (not recommended), run `pip install --pre scrapeo` since Scrapeo is still in pre-release


### Concept ###
* Scrape and analyze elements like meta data and content from web pages
* Provide a quick and easy-to-use tool for those who prefer command-line interfaces
* Provide useful analytical and assessment data


### Features ###
* Installation via `pip` or `make`
* Scrape pages from the command-line for meta tags by attribute-value pairs or by a single attribute's value
* Useful shortcuts like `-d` to get a page's meta description, or `-c` to retrieve a canonical URL
* Makefile for common development tasks, like building wheel, source, and deb packages


### Make commands ###


* **make test** - run all tests
* **make deb** - build Debian package (*requires system packages in requirements-dev.txt*)
* **make source** - build source tarball
* **make wheel** - build Python wheel
* **make daily** - make daily snapshot
* **make deploy** - create vitrual environment and install
* **make install** - install program
* **make init** - install all requirements
* **make clean** - clean project, remove .pyc and other temporary files


### Project Structure ###


```
    |-- docs
    |   |-- build
    |   |   |--doctrees
    |   |   `--text
    |   |      `-- index.txt
    |   |-- Makefile
    |   `-- source
    |       |-- conf.py
    |       `-- index.rst
    |-- scrapeo
    |   |-- __init__.py
    |   |-- utils
    |   |   |-- __init__.py
    |   |   `-- web_scraper.py
    |   |-- __init__.py
    |   |-- core.py
    |   |-- exceptions.py
    |   |-- main.py
    |   `-- helpers.py
    |-- tests
    |   |-- data
    |   |   `-- document.html
    |   |-- __init__.py
    |   |-- test_helpers.py
    |   `-- test_Scrapeo.py
    |-- CHANGES.txt
    |-- LICENSE.txt
    |-- MANIFEST.in
    |-- Makefile
    |-- README.md
    |-- README.rst
    |-- requirements-dev.txt
    |-- requirements.txt
    `-- setup.py
```

### Changelog ###

#### 0.1.1 ####
* Move from Python's html.parser to the external `html5lib` package to help deal with different forms of empty tags, eg. `<meta>` and `<meta />`
* Docs (generated using Sphinx and autodoc)
* Python 2 compatibility
* `-c` canonical link option added
* `-s` option for specifiying what element attribute to scrape a value from
* `-r` flag for scraping the content attribute of a robots meta tag
* `-H` option for scraping the text from the first heading by type (h1,h2,h3,etc.)
* Numerous bug fixes
* Test coverage

#### 0.1.0 ####
* Initial development release
