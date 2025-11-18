export enum SafeLevel {
  OFF = 'off',
  MEDIUM = 'medium',
  HIGH = 'high',
}

export interface SearchRequest {
  key: string;
  cx: string;
  q: string;
  start?: number;
  num?: number;
  safe?: SafeLevel;
  lr?: string;
}

export interface SearchResult {
  kind?: string;
  title?: string;
  htmlTitle?: string;
  link?: string;
  displayLink?: string;
  snippet?: string;
  htmlSnippet?: string;
  cacheId?: string;
  mime?: string;
  pagemap?: Record<string, any>;
}

export interface SearchResponse {
  kind?: string;
  url?: Record<string, any>;
  queries?: Record<string, any>;
  context?: Record<string, any>;
  searchInformation?: Record<string, any>;
  items?: SearchResult[];
}
