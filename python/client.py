import requests
import logging
from urllib.parse import urlencode
from typing import Optional, Dict, Any, List
from .models import SearchResponse
from .auth import GoogleCustomSearchApiKeyAuthHandler
from .errors import GoogleCustomSearchAPIError, GoogleCustomSearchAuthError

__version__ = "2.0.0"

class GoogleCustomSearchClient:
    """
    Client for Google Custom Search JSON API v2.
    
    Usage example:
        from google_custom_search.client import GoogleCustomSearchClient
        client = GoogleCustomSearchClient(api_key="YOUR_API_KEY", cx="YOUR_CSE_ID")
        resp = client.search(q="OpenAI GPT-4")
        print(resp)
    """

    BASE_URL = "https://www.googleapis.com/customsearch/v2"

    def __init__(self, *, api_key: str, cx: str, logger: Optional[logging.Logger] = None):
        if not api_key or len(api_key.strip()) < 10:
            raise ValueError("API key is missing or appears invalid.")
        if not cx or not cx.strip():
            raise ValueError("Custom Search Engine ID (cx) is required.")
        self.api_key = api_key
        self.cx = cx
        self.session = requests.Session()
        self.auth_handler = GoogleCustomSearchApiKeyAuthHandler(self.api_key)
        self.logger = logger or logging.getLogger(__name__)

    def search(self, 
               q: str,
               start: Optional[int] = None,
               num: Optional[int] = None,
               safe: Optional[str] = None,
               lr: Optional[str] = None,
               sort: Optional[str] = None,
               filter: Optional[str] = None,
               gl: Optional[str] = None,
               dateRestrict: Optional[str] = None,
               extra_params: Optional[Dict[str,Any]] = None
    ) -> SearchResponse:
        """
        Perform a search query.

        Params:
            q (str): Query string.
            start (Optional[int]): Index of the first result to return (pagination).
            num (Optional[int]): Number of search results to return.
            safe (Optional[str]): SafeSearch filter.
            lr (Optional[str]): Restrict by language (e.g., lang_en).
            sort (Optional[str]): Sort search results.
            filter (Optional[str]): Duplicate filtering.
            gl (Optional[str]): Geolocation.
            dateRestrict (Optional[str]): Restrict recency.
            extra_params (Optional[dict]): Additional parameters.

        Returns:
            SearchResponse: Parsed result object.
        """
        params = {
            "q": q,
            "cx": self.cx,
            "key": self.api_key,
        }
        if start is not None:
            params["start"] = start
        if num is not None:
            params["num"] = num
        if safe is not None:
            params["safe"] = safe
        if lr is not None:
            params["lr"] = lr
        if sort is not None:
            params["sort"] = sort
        if filter is not None:
            params["filter"] = filter
        if gl is not None:
            params["gl"] = gl
        if dateRestrict is not None:
            params["dateRestrict"] = dateRestrict

        if extra_params:
            params.update(extra_params)

        req = requests.Request("GET", self.BASE_URL, params=params)
        prepped = self.session.prepare_request(req)
        prepped = self.auth_handler.authenticate(prepped)

        try:
            resp = self.session.send(prepped)
        except requests.RequestException as e:
            self.logger.error(f"Network error while querying Custom Search API: {e}")
            raise GoogleCustomSearchAPIError(f"Network error while querying API: {e}")

        if resp.status_code in (401, 403):
            raise GoogleCustomSearchAuthError("Authentication failed: Invalid or expired API key.")
        if resp.status_code != 200:
            raise GoogleCustomSearchAPIError(f"API error {resp.status_code}: {resp.text}")

        try:
            result = resp.json()
        except Exception as e:
            self.logger.error(f"Failed to parse response as JSON: {e}")
            raise GoogleCustomSearchAPIError("Failed to parse API response as JSON.")

        return SearchResponse.from_dict(result)

