import requests
from typing import Optional, Dict, Any, List
from models import CustomSearchResponse
from auth import APIKeyAuth
from errors import APIError

__version__ = "1.0.0"

class GoogleCustomSearchClient:
    """Client for Google Custom Search JSON API.
    Docs: https://developers.google.com/custom-search/v1/overview
    """
    BASE_URL = 'https://www.googleapis.com/customsearch/v1'

    def __init__(self, api_key: str):
        self.auth = APIKeyAuth(api_key)
        self.session = requests.Session()
        self.session.hooks['response'].append(self._check_response)

    def search(
        self,
        cx: str,
        q: str,
        start: Optional[int] = None,
        num: Optional[int] = None,
        safe: Optional[str] = None,
        lr: Optional[str] = None,
        filter: Optional[str] = None,
        gl: Optional[str] = None,
        cr: Optional[str] = None,
        fileType: Optional[str] = None,
        imgType: Optional[str] = None,
        imgSize: Optional[str] = None,
        siteSearch: Optional[str] = None,
        siteSearchFilter: Optional[str] = None,
        sort: Optional[str] = None,
        fields: Optional[str] = None
    ) -> CustomSearchResponse:
        """Perform a custom search.

        Args:
            cx (str): The search engine ID to use (custom search engine CX).
            q (str): The query string.
            start (Optional[int]): Index of the first result to return (for pagination).
            num (Optional[int]): Number of search results to return.
            safe (Optional[str]): SafeSearch filtering level.
            lr (Optional[str]): Restrict results to a language.
            filter (Optional[str]), gl (Optional[str]), cr (Optional[str]), fileType (Optional[str]), ...: Other optional params from the API spec.

        Returns:
            CustomSearchResponse: Custom search result object.

        Raises:
            APIError: On HTTP or API error.
        """
        params: Dict[str, Any] = {
            'key': self.auth.api_key,
            'cx': cx,
            'q': q
        }
        if start is not None:
            params['start'] = start
        if num is not None:
            params['num'] = num
        if safe is not None:
            params['safe'] = safe
        if lr is not None:
            params['lr'] = lr
        if filter is not None:
            params['filter'] = filter
        if gl is not None:
            params['gl'] = gl
        if cr is not None:
            params['cr'] = cr
        if fileType is not None:
            params['fileType'] = fileType
        if imgType is not None:
            params['imgType'] = imgType
        if imgSize is not None:
            params['imgSize'] = imgSize
        if siteSearch is not None:
            params['siteSearch'] = siteSearch
        if siteSearchFilter is not None:
            params['siteSearchFilter'] = siteSearchFilter
        if sort is not None:
            params['sort'] = sort
        if fields is not None:
            params['fields'] = fields
        resp = self.session.get(self.BASE_URL, params=params)
        resp.raise_for_status()
        return CustomSearchResponse.from_dict(resp.json())

    def _check_response(self, r, *args, **kwargs):
        if not r.ok:
            raise APIError(f"API request failed: {r.status_code} {r.text}")
