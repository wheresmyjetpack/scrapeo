python-package-template
=======================

Start template for python package.  

### Usage ###
1. Run `git clone git://github.com/wheresmyjetpack/scrapeo.git`


### Concept ###
* **One location for settings** - all settings specified in **setup.py** only
* **Simple usage** - one command: **make**


### Features ###
* setup.py - all distutils, setuptools features
* tests - unittest, pytest
* .tar.gz - source generation
* .deb generation
* _.rpm generation_
* virtualenv - install and put package into it


### More commands ###
* **make test** - run all tests
* **make deb** - build Debian package
* **make source** - build source tarball
* **make daily** - make daily snapshot
* **make install** - install program
* **make init** - install all requirements
* **make clean** - clean project, remove *.pyc and other templorary files
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
