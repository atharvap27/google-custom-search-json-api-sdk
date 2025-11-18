# Google Custom Search JSON API Python SDK

## Installation

```bash
pip install .
```

## Usage

```python
from client import GoogleCustomSearchClient
from models import SafeLevel

client = GoogleCustomSearchClient(api_key="YOUR_API_KEY", cx="YOUR_CSE_ID")
result = client.search(q="OpenAI", safe=SafeLevel.MEDIUM)
for item in result.items or []:
    print(item.title, item.link)
```

## Version

This package is version 1.0.0, matching the API version v1.
