pho: High performance HTML parser built on lxml
===============================================

.. image:: https://secure.travis-ci.org/daniyalzade/pho.png
        :target: https://secure.travis-ci.org/daniyalzade/pho


pho is a library built on lxml, and implements the `Beautiful Soup <http://www.crummy.com/software/BeautifulSoup/>`_ apis. It is meant to be a drop in replacement for BS.

BS is an awesome library for parsing and navigating DOM. But, because it tries
to do a lot, it exhibits fairly poor performance. See `this post <http://blog.dispatched.ch/2010/08/16/beautifulsoup-vs-lxml-performance/>_` to see that directly using lxml over soup could give up to 70x speed improvement.

Pho aims to ease the transition from soup to using pure lxml, by implementing
a part of the soup API as thin wrapper on lxml. Though I don't have rigorous benchmarks, I have seen 10-30x performance improvement from using pho.

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

Source
------

You can see the code `here <https://github.com/daniyalzade/pho>`_
