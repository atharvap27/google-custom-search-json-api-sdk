def add_api_key(params: dict, api_key: str) -> dict:
    params['key'] = api_key
    return params
