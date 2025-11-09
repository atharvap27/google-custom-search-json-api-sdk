import { AxiosRequestConfig } from 'axios';

export class GoogleCustomSearchApiKeyAuthHandler {
  private apiKey: string;

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  authenticate(config: AxiosRequestConfig, credentials?: { api_key?: string }): AxiosRequestConfig {
    const key = credentials?.api_key || this.apiKey;
    if (!key) {
      throw new Error('API key is required for authentication.');
    }
    if (!config.params) config.params = {};
    config.params['key'] = key;
    return config;
  }

  refreshCredentials(_expiredCredentials: any): never {
    throw new Error('API Key authentication does not support refresh flow.');
  }

  validateCredentials(credentials?: { api_key?: string }): { valid: boolean; reason?: string } {
    const key = credentials?.api_key || this.apiKey;
    if (!key || typeof key !== 'string' || key.trim().length < 10) {
      return { valid: false, reason: 'API key is missing or appears invalid.' };
    }
    return { valid: true };
  }
}
