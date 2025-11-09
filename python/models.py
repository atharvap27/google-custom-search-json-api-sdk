from typing import Any, Dict, List, Optional

class QueryInfo:
    def __init__(self, title: str, searchTerms: str, count: int, startIndex: int):
        self.title = title
        self.searchTerms = searchTerms
        self.count = count
        self.startIndex = startIndex

    @staticmethod
    def from_dict(obj: Dict[str, Any]) -> 'QueryInfo':
        return QueryInfo(
            title=obj.get('title', ''),
            searchTerms=obj.get('searchTerms', ''),
            count=obj.get('count', 0),
            startIndex=obj.get('startIndex', 1)
        )

class SearchInformation:
    def __init__(self, searchTime: float, formattedSearchTime: str, totalResults: str, formattedTotalResults: str):
        self.searchTime = searchTime
        self.formattedSearchTime = formattedSearchTime
        self.totalResults = totalResults
        self.formattedTotalResults = formattedTotalResults

    @staticmethod
    def from_dict(obj: Dict[str, Any]) -> 'SearchInformation':
        return SearchInformation(
            searchTime=obj.get('searchTime', 0.0),
            formattedSearchTime=obj.get('formattedSearchTime', ''),
            totalResults=obj.get('totalResults', '0'),
            formattedTotalResults=obj.get('formattedTotalResults', '')
        )

class Context:
    def __init__(self, title: Optional[str]=None):
        self.title = title
    @staticmethod
    def from_dict(obj: Dict[str, Any]) -> 'Context':
        return Context(title=obj.get('title'))

class SearchResult:
    def __init__(self, kind: str, title: str, link: str, snippet: str, displayLink: Optional[str]=None, cacheId: Optional[str]=None, mime: Optional[str]=None):
        self.kind = kind
        self.title = title
        self.link = link
        self.snippet = snippet
        self.displayLink = displayLink
        self.cacheId = cacheId
        self.mime = mime

    @staticmethod
    def from_dict(obj: Dict[str, Any]) -> 'SearchResult':
        return SearchResult(
            kind=obj.get('kind', ''),
            title=obj.get('title', ''),
            link=obj.get('link', ''),
            snippet=obj.get('snippet', ''),
            displayLink=obj.get('displayLink'),
            cacheId=obj.get('cacheId'),
            mime=obj.get('mime')
        )

class CustomSearchResponse:
    def __init__(self, kind: str, items: Optional[List[SearchResult]]=None, queries: Optional[Dict[str, List[QueryInfo]]] = None, context: Optional[Context] = None, searchInformation: Optional[SearchInformation]=None):
        self.kind = kind
        self.items = items or []
        self.queries = queries or {}
        self.context = context
        self.searchInformation = searchInformation

    @staticmethod
    def from_dict(obj: Dict[str, Any]) -> 'CustomSearchResponse':
        items = [SearchResult.from_dict(x) for x in obj.get('items', [])]
        queries = {k: [QueryInfo.from_dict(q) for q in v] for k, v in obj.get('queries', {}).items()}
        context = Context.from_dict(obj.get('context', {})) if obj.get('context') else None
        searchInformation = SearchInformation.from_dict(obj.get('searchInformation', {})) if obj.get('searchInformation') else None
        return CustomSearchResponse(
            kind=obj.get('kind', ''),
            items=items,
            queries=queries,
            context=context,
            searchInformation=searchInformation
        )
