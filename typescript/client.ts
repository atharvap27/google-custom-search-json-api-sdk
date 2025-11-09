import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';
import { SearchResponse } from './models';
import { GoogleCustomSearchApiKeyAuthHandler } from './auth';
import { GoogleCustomSearchAPIError, GoogleCustomSearchAuthError } from './errors';

export const VERSION = '2.0.0';

export interface SearchParams {
  q: string;
  cx: string;
  start?: number;
  num?: number;
  safe?: string;
  lr?: string;
  sort?: string;
  filter?: string;
  gl?: string;
  dateRestrict?: string;
  [key: string]: any;
}

export class GoogleCustomSearchClient {
  private baseUrl = 'https://www.googleapis.com/customsearch/v2';
  private apiKey: string;
  private cx: string;
  private axios: AxiosInstance;
  private authHandler: GoogleCustomSearchApiKeyAuthHandler;

  constructor(apiKey: string, cx: string) {
    if (!apiKey || apiKey.trim().length < 10) {
      throw new Error('API key is missing or appears invalid.');
    }
    if (!cx || !cx.trim()) {
      throw new Error('Custom Search Engine ID (cx) is required.');
    }
    this.apiKey = apiKey;
    this.cx = cx;
    this.axios = axios.create();
    this.authHandler = new GoogleCustomSearchApiKeyAuthHandler(this.apiKey);
  }

  async search(params: Omit<SearchParams, 'key' | 'cx'> & { cx?: string }): Promise<SearchResponse> {
    const reqParams: any = {
      ...params,
      cx: params.cx || this.cx,
      key: this.apiKey
    };
    delete reqParams['key']; // Auth handler will inject
    const config: AxiosRequestConfig = {
      method: 'GET',
      url: this.baseUrl,
      params: reqParams,
    };

    this.authHandler.authenticate(config);

    let response: AxiosResponse<any>;
    try {
      response = await this.axios.request(config);
    } catch (e: any) {
      if (e.response && (e.response.status === 401 || e.response.status === 403)) {
        throw new GoogleCustomSearchAuthError('Authentication failed: Invalid or expired API key.');
      }
      throw new GoogleCustomSearchAPIError(`Network/API error: ${e.message}`);
    }
    if (response.status !== 200) {
      throw new GoogleCustomSearchAPIError(`API error ${response.status}: ${response.statusText}`);
    }
    return SearchResponse.fromJSON(response.data);
  }
}
