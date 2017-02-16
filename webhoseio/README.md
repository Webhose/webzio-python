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
