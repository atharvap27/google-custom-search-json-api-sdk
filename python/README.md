# Google Custom Search Python SDK

**Version: 2.0.0**

A Python SDK for the Google Custom Search JSON API (v2) with advanced filtering, safe search, sorting, geolocation, and recency options.

## Features
- Perform programmable custom searches
- Supports all v2 query params: sorting, filtering, safe search, locale, recency, etc.
- Proper error handling (network, API, and auth errors)
- Model classes for parsing results
- API key authentication via query param

## Installation

```
pip install google-customsearch-sdk
```
## Usage

```python
from google_custom_search.client import GoogleCustomSearchClient
client = GoogleCustomSearchClient(api_key="YOUR_API_KEY", cx="YOUR_CSE_ID")
result = client.search(q="OpenAI GPT-4", num=3)
print(result.items[0].title, result.items[0].link)
```
## API Key Setup
Set the `GOOGLE_CSE_API_KEY` environment variable or pass `api_key` directly.

## Classes
- `GoogleCustomSearchClient` – The main API client
- `GoogleCustomSearchApiKeyAuthHandler` – Auth handler
- `ResultItem`, `SearchInformation`, `SearchResponse` – Data models

## Parameters
- `q`, `start`, `num`, `safe`, `lr`, `sort`, `filter`, `gl`, `dateRestrict`, `cx`, `key`

## Error Handling
- `GoogleCustomSearchAPIError` (general)
- `GoogleCustomSearchAuthError` (auth issues, 401/403)

## License
Apache 2.0
