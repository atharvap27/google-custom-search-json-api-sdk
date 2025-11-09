export interface ResultItem {
  title: string;
  link: string;
  snippet: string;
  relevanceScore?: number;
  [key: string]: any;
}

export interface SearchInformation {
  totalResults: string;
  searchTime: number;
  formattedSearchTime?: string;
}

export interface SearchResponseLike {
  items: ResultItem[];
  searchInformation?: SearchInformation;
  [key: string]: any;
}

export class SearchResponse {
  items: ResultItem[];
  searchInformation?: SearchInformation;
  raw: any;

  constructor(data: SearchResponseLike) {
    this.items = data.items || [];
    this.searchInformation = data.searchInformation;
    this.raw = data;
  }

  static fromJSON(json: any): SearchResponse {
    return new SearchResponse(json);
  }
}
