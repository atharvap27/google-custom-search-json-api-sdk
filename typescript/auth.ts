// No OAuth: API Key is included in payload per request
export class APIKeyAuth {
  private apiKey: string;
  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }
}
