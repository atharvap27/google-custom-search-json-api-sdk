# Google Custom Search SDK (TypeScript)

This SDK provides a strongly-typed interface to the [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview).

## Installation

```bash
npm install google-custom-search-sdk
```

## Usage

```typescript
import { GoogleCustomSearchClient } from './client';

const client = new GoogleCustomSearchClient('YOUR_KEY');

(async () => {
    const results = await client.search('YOUR_CX', 'typescript sdk');
    for (const item of results.items) {
        console.log(item.title, item.link);
    }
})();
```

All parameters and returned types are provided as strict TypeScript types.

Optional parameters for `search` (see models and client): start, num, safe, lr, filter, gl, cr, fileType, imgType, imgSize, siteSearch, siteSearchFilter, sort, fields.

## Version

1.0.0
