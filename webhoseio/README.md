webhose.io client for Python
============================
A simple way to access the [Webhose.io](https://webhose.io) API from your Python code
```python

    import webhoseio

    webhoseio.config(token=YOUR_API_KEY)
    output = webhoseio.query("filterWebData", {"q":"github"})
    print output['posts'][0]['text'] # Print the text of the first post
    print output['posts'][0]['published'] # Print the text of the first post publication date
    
    # Get the next batch of posts
    output = webhoseio.get_next()
    print output['posts'][0]['thread']['site'] # Print the site of the first post
    

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
    $ cd webhose-python
    $ python setup.py install
    
 ```
 
 Use the API
-----------

To get started, you need to import the library, and set your access token.
(Replace YOUR_API_KEY with your actual API key).

```python

    >>> import webhoseio
    >>> webhoseio.config(token=YOUR_API_KEY)
```

Now you can make a request and inspect the results:

```python

    >>> output = webhoseio.query("filterWebData", {"q":"github"})
    >>> output['totalResults']
    15565094
    len(output['posts'])
    100
    >>> output['posts'][0]['language']
    u'english'
    >>> output['posts'][0]['title']
    u'Putting quotes around dictionary keys in JS'
```


For your convenience, the Response object is iterable, so you can loop over it
and get all the results. The iterator will create additional API requests to
fetch additional pages.

````python

    >>> total_words = 0
    >>> for post in output['posts']:
    ...     total_words += len(post['text'].split(" "))
    ...
    >>> print(total_words)
    8822
````    

**Warning**: This method can use up your credits if your search has lots of
results.
