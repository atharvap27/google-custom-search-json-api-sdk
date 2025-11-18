export type SafeEnum = 'off' | 'medium' | 'high';

export interface SearchRequest {
    key: string;
    cx: string;
    q: string;
    sort?: string;
    filter?: string;
    safe?: SafeEnum;
    lr?: string;
    num?: number;
    start?: number;
    cr?: string;
    gl?: string;
    hl?: string;
    siteSearch?: string;
    siteSearchFilter?: string;
    dateRestrict?: string;
    exactTerms?: string;
    excludeTerms?: string;
    fileType?: string;
    imgColorType?: string;
    imgDominantColor?: string;
    imgSize?: string;
    imgType?: string;
    linkSite?: string;
    orTerms?: string;
    relatedSite?: string;
    rights?: string;
    searchType?: string;
    fields?: string;
}

export interface QueryInfo {
    title?: string;
    totalResults?: string;
    searchTerms?: string;
    count?: number;
    startIndex?: number;
    inputEncoding?: string;
    outputEncoding?: string;
    safe?: string;
    cx?: string;
}

export interface SearchInformation {
    searchTime?: number;
    formattedSearchTime?: string;
    totalResults?: string;
    formattedTotalResults?: string;
}

export interface Context {
    title?: string;
}

export interface SearchItem {
    kind?: string;
    title?: string;
    htmlTitle?: string;
    link?: string;
    displayLink?: string;
    snippet?: string;
    htmlSnippet?: string;
    cacheId?: string;
    formattedUrl?: string;
    htmlFormattedUrl?: string;
    pagemap?: Record<string, any>;
}

export interface SearchResponse {
    kind?: string;
    url?: Record<string, any>;
    queries?: { [key: string]: QueryInfo[] };
    context?: Context;
    searchInformation?: SearchInformation;
    items?: SearchItem[];
    [key: string]: unknown;
}
