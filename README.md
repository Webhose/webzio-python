webhose.io client for Python
============================
A simple way to access the [Webhose.io](https://webhose.io) API from your Python code
```python

    import webhoseio
    
    webhoseio.config(token=YOUR_API_KEY)
    output = webhoseio.query("filterWebContent", {"q":"github"})
    print(output['posts'][0]['text'])           # Print the text of the first post
    print(output['posts'][0]['published'])      # Print the text of the first post publication date
    
    # Get the next batch of posts
    output = webhoseio.get_next()
    print(output['posts'][0]['thread']['site']) # Print the site of the first post

```

API Key
-------

To make use of the webhose.io API, you need to obtain a token that would be
used on every request. To obtain an API key, create an account at
https://webhose.io/auth/signup, and then go into
https://webhose.io/dashboard to see your token.


Installing
----------
You can install from source:

``` bash

    $ git clone https://github.com/Webhose/webhoseio-python
    $ cd webhoseio-python
    $ python setup.py install
    
 ```
 Or use pip install:
 
 ``` bash
    $ sudo pip install webhoseio
 ```
 
 Use the API
-----------

To get started, you need to import the library, and set your access token.
(Replace YOUR_API_KEY with your actual API key).

```python

    >>> import webhoseio
    >>> webhoseio.config(token=YOUR_API_KEY)      
```

**API Endpoints**

The first parameter the query() function accepts is the API endpoint string. Available endpoints:
* filterWebContent - access to the news/blogs/forums/reviews API

Now you can make a request and inspect the results:

```python

    >>> output = webhoseio.query("filterWebContent", {"q":"github"})
    >>> output['totalResults']
    15565094
    len(output['posts'])
    100
    >>> output['posts'][0]['language']
    u'english'
    >>> output['posts'][0]['title']
    u'Putting quotes around dictionary keys in JS'
```


For your convenience, the ouput object is iterable, so you can loop over it
and get all the results of this batch (up to 100). 

```python

    >>> total_words = 0
    >>> for post in output['posts']:
    ...     total_words += len(post['text'].split(" "))
    ...
    >>> print(total_words)
    8822
```    
Full documentation
------------------

* ``config(token)``

  * token - your API key

* ``query(end_point_str, params)``

  * end_point_str: 
    * filterWebContent - access to the news/blogs/forums/reviews API

  * params: A key value dictionary. The most common key is the "q" parameter that hold the filters Boolean query. [Read about the available filters](https://webhose.io/documentation).

* ``get_next()`` - a method to fetch the next page of results.
    
    
Polling
-------

If you want to make repeated searches, performing an action whenever there are
new results, use code like this:

``` python

    r = webhoseio.query("filterWebContent", {"q":"skyrim"})
    while True:
        for post in r['posts']:
            perform_action(post)
        time.sleep(300)
        r = webhoseio.get_next()
```        

