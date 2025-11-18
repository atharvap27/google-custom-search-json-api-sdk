import requests
import logging
from typing import Optional, Dict, Any, List
from .models import SearchResponse
from .errors import GoogleCustomSearchError
from .auth import add_api_key

__version__ = "1.0.0"

logger = logging.getLogger("google_custom_search_sdk")

class GoogleCustomSearchClient:
    BASE_URL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self,
               cx: str,
               q: str,
               sort: Optional[str] = None,
               filter: Optional[str] = None,
               safe: Optional[str] = None,
               lr: Optional[str] = None,
               num: Optional[int] = None,
               start: Optional[int] = None,
               cr: Optional[str] = None,
               gl: Optional[str] = None,
               hl: Optional[str] = None,
               siteSearch: Optional[str] = None,
               siteSearchFilter: Optional[str] = None,
               dateRestrict: Optional[str] = None,
               exactTerms: Optional[str] = None,
               excludeTerms: Optional[str] = None,
               fileType: Optional[str] = None,
               imgColorType: Optional[str] = None,
               imgDominantColor: Optional[str] = None,
               imgSize: Optional[str] = None,
               imgType: Optional[str] = None,
               linkSite: Optional[str] = None,
               orTerms: Optional[str] = None,
               relatedSite: Optional[str] = None,
               rights: Optional[str] = None,
               searchType: Optional[str] = None,
               fields: Optional[str] = None
        ) -> SearchResponse:
        """
        Perform a custom search. See Google Custom Search JSON API for parameter details.
        Returns:
            SearchResponse: Search results
        Raises:
            GoogleCustomSearchError
        """
        params = {
            "key": self.api_key,
            "cx": cx,
            "q": q,
        }
        OPTIONAL_PARAMS = [
            "sort","filter","safe","lr","num","start","cr","gl","hl","siteSearch","siteSearchFilter",
            "dateRestrict","exactTerms","excludeTerms","fileType","imgColorType","imgDominantColor","imgSize",
            "imgType","linkSite","orTerms","relatedSite","rights","searchType","fields"
        ]
        for param in OPTIONAL_PARAMS:
            val = locals().get(param)
            if val is not None:
                params[param] = val
        logger.debug(f"Sending GET to {self.BASE_URL} with params: {params}")
        try:
            response = requests.get(self.BASE_URL, params=params)
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise GoogleCustomSearchError(f"HTTP error: {e}")

        if response.status_code != 200:
            logger.error(f"Non-200 response: {response.text}")
            raise GoogleCustomSearchError(f"API error: {response.status_code} - {response.text}")

        try:
            result = response.json()
        except ValueError:
            logger.error("Failed to decode JSON response")
            raise GoogleCustomSearchError("Invalid JSON response from API")

        return SearchResponse.from_dict(result)
