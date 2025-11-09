import axios, { AxiosInstance, AxiosResponse } from 'axios';
import { CustomSearchResponse } from './models';
import { APIKeyAuth } from './auth';
import { APIError } from './errors';

export const VERSION = '1.0.0';

export class GoogleCustomSearchClient {
    private readonly baseUrl = 'https://www.googleapis.com/customsearch/v1';
    private readonly auth: APIKeyAuth;
    private readonly client: AxiosInstance;

    constructor(apiKey: string) {
        this.auth = new APIKeyAuth(apiKey);
        this.client = axios.create();

        this.client.interceptors.response.use(response => response,
            error => {
                if (error.response) {
                    throw new APIError(`API request failed: ${error.response.status} ${error.response.statusText}`);
                }
                throw error;
            });
    }

    /**
     * Perform a custom search.
     * @param cx The search engine ID to use (custom search engine CX).
     * @param q The query string.
     * @param start Index of the first result to return (for pagination).
     * @param num Number of search results to return.
     * @param safe SafeSearch filtering level.
     * @param lr Restrict results to a language.
     * @param filter Optional filtering.
     * @param gl Geolocation country.
     * @param cr Country restrict.
     * @param fileType File type filter.
     * @param imgType Image type.
     * @param imgSize Image size.
     * @param siteSearch Site to search.
     * @param siteSearchFilter Site search filter.
     * @param sort Sort results.
     * @param fields Fields to include.
     */
    async search(
        cx: string,
        q: string,
        start?: number,
        num?: number,
        safe?: string,
        lr?: string,
        filter?: string,
        gl?: string,
        cr?: string,
        fileType?: string,
        imgType?: string,
        imgSize?: string,
        siteSearch?: string,
        siteSearchFilter?: string,
        sort?: string,
        fields?: string
    ): Promise<CustomSearchResponse> {
        const params: Record<string, string | number | undefined> = {
            key: this.auth.apiKey,
            cx,
            q,
            start,
            num,
            safe,
            lr,
            filter,
            gl,
            cr,
            fileType,
            imgType,
            imgSize,
            siteSearch,
            siteSearchFilter,
            sort,
            fields
        };
        // Remove undefined
        Object.keys(params).forEach(key => params[key] === undefined && delete params[key]);
        const resp: AxiosResponse = await this.client.get(this.baseUrl, { params });
        return CustomSearchResponse.fromObject(resp.data);
    }
}
