#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(
        name='scrapeo',
        version='0.1.0.dev2',
        author='Paul Morris',
        author_email='wheresmyjetpack03@gmail.com',
        #url='http://www.scrapeo.org',
        #download_url='http://www.scrapeo.org/files/',
        description='A command-line SEO web scraping / analysis tool',
        long_description='Provides a command-line client for scraping and analyzing relevant SEO data from webpages.',

        packages = find_packages(),
        include_package_data = True,
        package_data = {
            '': ['*.txt', '*.rst'],
            'scrapeo': ['data/*.html', 'data/*.css'],
            },
        entry_points = {
            'console_scripts': [
                'scrapeo = scrapeo.main:main'
                ]
            },
        exclude_package_data = { '': ['README.txt'] },
        keywords='python tools utils internet www',
        license='GPL',
        classifiers=['Development Status :: 2 - Pre-Alpha',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Topic :: Internet',
            'Topic :: Internet :: WWW/HTTP',
            ],

        install_requires = ['setuptools', 'beautifulsoup4', 'requests'],
        )
