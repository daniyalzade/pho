# -*- coding: utf-8 -*-
"""
pho: High performance HTML parser built on lxml
===============================================

pho is a library built on lxml, and implements the [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) apis. It is meant to be a drop in replacement for BS.


Installation
------------

To install requests, simply: ::

    $ pip install pho

Pho tries to pip install lxml, and for lxml you will need the following packages installed in your system.


Usage
------

    import pho
    import requests

    Pho(requests.get('http://google.com').content).find('title').get_text()
"""

from setuptools import setup

requires = [
        'lxml'
        ]

packages = [
    'pho',
]

setup(
    name='pho',
    author='Eytan Daniyalzade',
    author_email='eytan@stylrapp.com',
    url='http://stylrapp.com',
    packages=packages,
    description='High performance HTML parser built on lxml',
    long_description=__doc__,
    install_requires=requires,
    version='0.0.3',
    package_dir={
        'pho': 'pho'
        },
)
