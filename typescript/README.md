# Google Custom Search TypeScript SDK

A TypeScript SDK for Google Custom Search JSON API.

## Installation

```bash
npm install google-custom-search
```

## Usage

```typescript
import { GoogleCustomSearchClient } from './client';

const client = new GoogleCustomSearchClient('YOUR_API_KEY');
client.search({ cx: 'YOUR_CSE_ID', q: 'openai' })
  .then(res => {
    if (res.items) {
      res.items.forEach(item => {
        console.log(item.title, item.link);
      });
    }
  })
  .catch(err => {
    console.error(err);
  });
```

## All Parameters
See https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list for all parameters and options.
