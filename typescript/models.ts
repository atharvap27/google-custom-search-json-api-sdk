/** Strongly-typed models for the Google Custom Search API */
export interface QueryInfo {
    title: string;
    searchTerms: string;
    count: number;
    startIndex: number;
}

export interface Context {
    title?: string;
}

export interface SearchInformation {
    searchTime: number;
    formattedSearchTime: string;
    totalResults: string;
    formattedTotalResults: string;
}

export interface SearchResult {
    kind: string;
    title: string;
    link: string;
    snippet: string;
    displayLink?: string;
    cacheId?: string;
    mime?: string;
}

export interface Queries {
    [key: string]: QueryInfo[];
}

export class CustomSearchResponse {
    kind: string;
    items: SearchResult[];
    queries: Queries;
    context?: Context;
    searchInformation?: SearchInformation;

    constructor(kind: string, items: SearchResult[], queries: Queries, context?: Context, searchInformation?: SearchInformation) {
        this.kind = kind;
        this.items = items;
        this.queries = queries;
        this.context = context;
        this.searchInformation = searchInformation;
    }

    static fromObject(obj: any): CustomSearchResponse {
        return new CustomSearchResponse(
            obj.kind ?? '',
            (obj.items ?? []).map((item: any): SearchResult => ({
                kind: item.kind ?? '',
                title: item.title ?? '',
                link: item.link ?? '',
                snippet: item.snippet ?? '',
                displayLink: item.displayLink,
                cacheId: item.cacheId,
                mime: item.mime
            })),
            Object.fromEntries(
                Object.entries(obj.queries || {}).map(([key, queryArr]: [string, any[]]) => [key, queryArr.map((q: any): QueryInfo => ({
                    title: q.title,
                    searchTerms: q.searchTerms,
                    count: q.count,
                    startIndex: q.startIndex
                }))])
            ),
            obj.context ? { title: obj.context.title } : undefined,
            obj.searchInformation ? {
                searchTime: obj.searchInformation.searchTime,
                formattedSearchTime: obj.searchInformation.formattedSearchTime,
                totalResults: obj.searchInformation.totalResults,
                formattedTotalResults: obj.searchInformation.formattedTotalResults
            } : undefined
        );
    }
}
