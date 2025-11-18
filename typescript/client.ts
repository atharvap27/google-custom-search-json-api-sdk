import axios, { AxiosResponse } from 'axios';
import { SearchRequest, SearchResponse } from './models';
import { GoogleCustomSearchError } from './errors';
import { addApiKey } from './auth';

export const VERSION = "1.0.0";

export class GoogleCustomSearchClient {
    private baseUrl: string = 'https://www.googleapis.com/customsearch/v1';
    private apiKey: string;

    constructor(apiKey: string) {
        this.apiKey = apiKey;
    }

    async search(params: Omit<SearchRequest, 'key'>): Promise<SearchResponse> {
        const payload = addApiKey(params, this.apiKey);
        try {
            const response: AxiosResponse<SearchResponse> = await axios.get<SearchResponse>(this.baseUrl, { params: payload });
            return response.data;
        } catch (e: any) {
            if (e.response) {
                throw new GoogleCustomSearchError(`API error: ${e.response.status} - ${e.response.data}`);
            } else {
                throw new GoogleCustomSearchError(e.message);
            }
        }
    }
}
