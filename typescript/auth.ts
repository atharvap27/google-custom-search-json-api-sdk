export function addApiKey(params: Record<string, any>, apiKey: string): Record<string, any> {
    return { ...params, key: apiKey };
}
