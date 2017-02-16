webhose.io client for Python
============================
A simple way to access the [Webhose.io](https://webhose.io) API from your Python code
```python

    import webhoseio

    webhoseio.config(token=YOUR_API_KEY)
    output = webhoseio.query("filterWebData", {"q":"github"})
    print output

```
