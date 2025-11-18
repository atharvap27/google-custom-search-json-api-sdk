import requests
import logging
from typing import Optional, Dict
from .models import SearchRequest, SearchResponse, SafeLevel
from .errors import GoogleAPIError

__version__ = "1.0.0"

class GoogleCustomSearchClient:
    def __init__(self, api_key: str, cx: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.cx = cx
        self.base_url = base_url or 'https://www.googleapis.com/customsearch/v1'
        self.session = requests.Session()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('GoogleCustomSearchClient')

    def search(self, q: str, start: Optional[int] = None, num: Optional[int] = None,
               safe: Optional[SafeLevel] = None, lr: Optional[str] = None) -> SearchResponse:
        url = self.base_url
        payload = {
            'key': self.api_key,
            'cx': self.cx,
            'q': q
        }
        if start is not None:
            payload['start'] = start
        if num is not None:
            payload['num'] = num
        if safe is not None:
            payload['safe'] = safe.value
        if lr is not None:
            payload['lr'] = lr
        headers = {'Content-Type': 'application/json'}
        self.logger.info(f'Performing search with query: {q}')
        response = self.session.post(url, json=payload, headers=headers)
        if not response.ok:
            self.logger.error(f'Request failed: {response.status_code} - {response.text}')
            raise GoogleAPIError(f'API request failed: {response.status_code} - {response.text}')
        return SearchResponse.parse_obj(response.json())
