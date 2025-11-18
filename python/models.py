from typing import Optional, List, Dict, Any
from enum import Enum
from pydantic import BaseModel

class SafeLevel(str, Enum):
    OFF = 'off'
    MEDIUM = 'medium'
    HIGH = 'high'

class SearchRequest(BaseModel):
    key: str
    cx: str
    q: str
    start: Optional[int] = None
    num: Optional[int] = None
    safe: Optional[SafeLevel] = None
    lr: Optional[str] = None

class SearchResult(BaseModel):
    kind: Optional[str]
    title: Optional[str]
    htmlTitle: Optional[str]
    link: Optional[str]
    displayLink: Optional[str]
    snippet: Optional[str]
    htmlSnippet: Optional[str]
    cacheId: Optional[str]
    mime: Optional[str]
    pagemap: Optional[Dict[str, Any]]
    # Add more fields as per OpenAPI schemas if present

class SearchResponse(BaseModel):
    kind: Optional[str]
    url: Optional[Dict[str, Any]]
    queries: Optional[Dict[str, Any]]
    context: Optional[Dict[str, Any]]
    searchInformation: Optional[Dict[str, Any]]
    items: Optional[List[SearchResult]]
