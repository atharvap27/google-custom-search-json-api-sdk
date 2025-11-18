# Google Custom Search Python SDK

A Python SDK for Google Custom Search JSON API.

## Installation

```bash
pip install .
```

## Usage

```python
from google_custom_search.client import GoogleCustomSearchClient

client = GoogleCustomSearchClient(api_key="YOUR_API_KEY")
res = client.search(cx="YOUR_CSE_ID", q="openai")
for item in res.items:
    print(item.title, item.link)
```

## All Parameters
| Name             | Required | Description |
|------------------|----------|-------------|
| cx               | yes      | Custom Search Engine ID |
| q                | yes      | Search Query           |
| ...              | ...      | See https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list for all options |
