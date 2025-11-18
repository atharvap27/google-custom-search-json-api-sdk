import axios, { AxiosInstance } from 'axios';
import { SearchRequest, SearchResponse, SafeLevel } from './models';
import { GoogleAPIError } from './errors';

export const VERSION = '1.0.0';

export class GoogleCustomSearchClient {
  private apiKey: string;
  private cx: string;
  private baseUrl: string;
  private axiosInstance: AxiosInstance;

  constructor(apiKey: string, cx: string, baseUrl: string = 'https://www.googleapis.com/customsearch/v1') {
    this.apiKey = apiKey;
    this.cx = cx;
    this.baseUrl = baseUrl;
    this.axiosInstance = axios.create();
  }

  async search(q: string, start?: number, num?: number, safe?: SafeLevel, lr?: string): Promise<SearchResponse> {
    const payload: SearchRequest = {
      key: this.apiKey,
      cx: this.cx,
      q
    };
    if (start !== undefined) payload.start = start;
    if (num !== undefined) payload.num = num;
    if (safe !== undefined) payload.safe = safe;
    if (lr !== undefined) payload.lr = lr;
    try {
      const response = await this.axiosInstance.post(this.baseUrl, payload, {
        headers: { 'Content-Type': 'application/json' }
      });
      return response.data as SearchResponse;
    } catch (error: any) {
      throw new GoogleAPIError(error.response?.status, error.response?.data || error.message);
    }
  }
}
