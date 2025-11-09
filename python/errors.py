class GoogleCustomSearchAPIError(Exception):
    """Raised for non-auth Google Custom Search API errors."""
    pass

class GoogleCustomSearchAuthError(Exception):
    """Raised for API authentication errors."""
    pass
