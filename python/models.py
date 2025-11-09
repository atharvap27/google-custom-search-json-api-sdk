from typing import List, Dict, Optional, Any

class ResultItem:
    def __init__(self, title: str, link: str, snippet: str, relevanceScore: Optional[float] = None, **kwargs):
        self.title = title
        self.link = link
        self.snippet = snippet
        self.relevanceScore = relevanceScore
        self.extra = kwargs

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            title=d.get("title", ""),
            link=d.get("link", ""),
            snippet=d.get("snippet", ""),
            relevanceScore=d.get("relevanceScore"),
            **{k:v for k,v in d.items() if k not in {"title", "link", "snippet", "relevanceScore"}}
        )

    def __repr__(self):
        return f"<ResultItem title={self.title!r} link={self.link!r}>"

class SearchInformation:
    def __init__(self, totalResults: str, searchTime: float, formattedSearchTime: Optional[str]=None):
        self.totalResults = totalResults
        self.searchTime = searchTime
        self.formattedSearchTime = formattedSearchTime

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            totalResults=d.get("totalResults", "0"),
            searchTime=d.get("searchTime", 0.0),
            formattedSearchTime=d.get("formattedSearchTime")
        )

    def __repr__(self):
        return f"<SearchInformation totalResults={self.totalResults} searchTime={self.searchTime}>"

class SearchResponse:
    def __init__(self, items: List[ResultItem], searchInformation: Optional[SearchInformation], raw: Dict[str, Any]):
        self.items = items
        self.searchInformation = searchInformation
        self.raw = raw

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        items = [ResultItem.from_dict(it) for it in d.get("items", [])]
        info = None
        if "searchInformation" in d:
            info = SearchInformation.from_dict(d.get("searchInformation", {}))
        return cls(items=items, searchInformation=info, raw=d)

    def __repr__(self):
        return f"<SearchResponse items={len(self.items)} searchInformation={self.searchInformation}>"
