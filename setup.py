from codecs import open
from pathlib import Path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = '''
============================
webz.io client for Python
============================
A simple way to access the `Webz.io <https://webz.io/>`_ API from your Python code::
.. code-block:: python

    import webzio

    webzio.config(token=YOUR_API_KEY)
    output = webzio.query("filterWebContent", {"q":"github"})
    print output['posts'][0]['text'] # Print the text of the first post
    print output['posts'][0]['published'] # Print the text of the first post publication date

    # Get the next batch of posts
    output = webzio.get_next()
    print output['posts'][0]['thread']['site'] # Print the site of the first post

API Key
-------

To make use of the webz.io API, you need to obtain a token that would be
used on every request. To obtain an API key, create an account at
https://webz.io/auth/signup, and then go into
https://webz.io/dashboard to see your token.


Installing
----------
You can install from source:

.. code-block:: bash

    $ git clone https://github.com/webz.io/webzio-python
    $ cd webzio-python
    $ python setup.py install

Or use pip install:

.. code-block:: bash
    
    $ sudo pip install webzio

Use the API
-----------

To get started, you need to import the library, and set your access token.
(Replace YOUR_API_KEY with your actual API key).

.. code-block:: python

    >>> import webzio
    >>> webzio.config(token=YOUR_API_KEY)

**API Endpoints**

The first parameter the query() function accepts is the API endpoint string. Available endpoints:
* filterWebContent - access to the news/blogs/forums/reviews API

Now you can make a request and inspect the results:

.. code-block:: python

    >>> output = webzio.query("filterWebContent", {"q":"github"})
    >>> output['totalResults']
    15565094
    len(output['posts'])
    100
    >>> output['posts'][0]['language']
    u'english'
    >>> output['posts'][0]['title']
    u'Putting quotes around dictionary keys in JS'

For your convenience, the ouput object is iterable, so you can loop over it
and get all the results of this batch (up to 100).

.. code-block:: python

    >>> total_words = 0
    >>> for post in output['posts']:
    ...     total_words += len(post['text'].split(" "))
    ...
    >>> print(total_words)
    8822

Full documentation
------------------

* ``config(token)``

  * token - your API key

* ``query(end_point_str, params)``

  * end_point_str:
    * filterWebContent - access to the news/blogs/forums/reviews API

  * params: A key value dictionary. The most common key is the "q" parameter that hold the filters Boolean query. [Read about the available filters](https://webz.io/documentation).

* ``get_next()`` - a method to fetch the next page of results.


Polling
-------

If you want to make repeated searches, performing an action whenever there are
new results, use code like this:

.. code-block:: python

    r = webzio.query("filterWebContent", {"q":"skyrim"})
    while True:
        for post in r['posts']:
            perform_action(post)
        time.sleep(300)
        r = webzio.get_next()
'''

setup(
    name='webzio',
    packages=['webzio'],
    version='1.0.2',
    author='Ran Geva',
    author_email='ran@webz.io',
    url='https://github.com/webhose/webzio-python',
    license='MIT',
    description='Simple client library for the webz.io REST API',
    long_description=long_description,
    install_requires=[
        "requests >= 2.0.0"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
