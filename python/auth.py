class GoogleCustomSearchApiKeyAuthHandler:
    """
    Handles injection of API key as a query parameter for Google Custom Search JSON API requests.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def authenticate(self, request, credentials=None):
        key = credentials.get('api_key') if credentials else self.api_key
        if not key:
            raise ValueError('API key is required for authentication.')
        # Works for requests.PreparedRequest
        from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
        url_parts = list(urlparse(request.url))
        query = parse_qs(url_parts[4])
        query['key'] = [key]
        url_parts[4] = urlencode(query, doseq=True)
        request.url = urlunparse(url_parts)
        return request

    def refresh_credentials(self, expired_credentials):
        raise NotImplementedError('API Key authentication does not support refresh flow.')

    def validate_credentials(self, credentials=None):
        key = credentials.get('api_key') if credentials else self.api_key
        if not key or not isinstance(key, str) or len(key.strip()) < 10:
            return {'valid': False, 'reason': 'API key is missing or appears invalid.'}
        return {'valid': True}
