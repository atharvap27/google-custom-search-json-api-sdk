# Google Custom Search JSON API TypeScript SDK

## Installation

```bash
npm install .
```

## Usage

```typescript
import { GoogleCustomSearchClient, SafeLevel } from './client';

const client = new GoogleCustomSearchClient("YOUR_API_KEY", "YOUR_CSE_ID");
client.search("OpenAI", undefined, undefined, SafeLevel.MEDIUM).then(result => {
  if (result.items) {
    for (const item of result.items) {
      console.log(item.title, item.link);
    }
  }
});
```

## Version

This package is version 1.0.0, matching the API version v1.
