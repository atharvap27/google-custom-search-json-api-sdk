# Google Custom Search SDK (Python)

This SDK provides a strongly-typed interface to the [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview).

## Installation

```bash
pip install .
```

## Usage

```python
from client import GoogleCustomSearchClient

client = GoogleCustomSearchClient(api_key="YOUR_KEY")

results = client.search(cx="YOUR_CX", q="python sdk")
for item in results.items:
    print(item.title, item.link)
```

Optional parameters for `search` (see models and client):
- start, num, safe, lr, filter, gl, cr, fileType, imgType, imgSize, siteSearch, siteSearchFilter, sort, fields.

## Version

1.0.0
