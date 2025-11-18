from typing import Optional, List, Dict, Any, Union

class SearchInformation:
    def __init__(self, data: Dict[str, Any]):
        self.search_time: Optional[float] = data.get("searchTime")
        self.formatted_search_time: Optional[str] = data.get("formattedSearchTime")
        self.total_results: Optional[str] = data.get("totalResults")
        self.formatted_total_results: Optional[str] = data.get("formattedTotalResults")

class QueryInfo:
    def __init__(self, data: Dict[str, Any]):
        self.title: Optional[str] = data.get("title")
        self.total_results: Optional[str] = data.get("totalResults")
        self.search_terms: Optional[str] = data.get("searchTerms")
        self.count: Optional[int] = data.get("count")
        self.start_index: Optional[int] = data.get("startIndex")
        self.input_encoding: Optional[str] = data.get("inputEncoding")
        self.output_encoding: Optional[str] = data.get("outputEncoding")
        self.safe: Optional[str] = data.get("safe")
        self.cx: Optional[str] = data.get("cx")

class Context:
    def __init__(self, data: Dict[str, Any]):
        self.title: Optional[str] = data.get("title")

class SearchItem:
    def __init__(self, data: Dict[str, Any]):
        self.kind: Optional[str] = data.get("kind")
        self.title: Optional[str] = data.get("title")
        self.html_title: Optional[str] = data.get("htmlTitle")
        self.link: Optional[str] = data.get("link")
        self.display_link: Optional[str] = data.get("displayLink")
        self.snippet: Optional[str] = data.get("snippet")
        self.html_snippet: Optional[str] = data.get("htmlSnippet")
        self.cache_id: Optional[str] = data.get("cacheId")
        self.formatted_url: Optional[str] = data.get("formattedUrl")
        self.html_formatted_url: Optional[str] = data.get("htmlFormattedUrl")
        self.pagemap: Optional[Dict[str, Any]] = data.get("pagemap")

class SearchResponse:
    def __init__(self, data: Dict[str, Any]):
        self.kind: Optional[str] = data.get("kind")
        self.url: Optional[Dict[str, Any]] = data.get("url")
        self.queries: Optional[Dict[str, List[QueryInfo]]] = None
        if "queries" in data:
            self.queries = {}
            for key, lst in data["queries"].items():
                self.queries[key] = [QueryInfo(q) for q in lst]
        self.context: Optional[Context] = Context(data["context"]) if "context" in data else None
        self.search_information: Optional[SearchInformation] = SearchInformation(data["searchInformation"]) if "searchInformation" in data else None
        self.items: Optional[List[SearchItem]] = [SearchItem(item) for item in data.get("items", [])]
        self.raw: Dict[str, Any] = data

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'SearchResponse':
        return SearchResponse(data)
