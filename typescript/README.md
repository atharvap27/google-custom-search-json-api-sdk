# Google Custom Search TypeScript SDK

**Version: 2.0.0**

A TypeScript SDK for the Google Custom Search JSON API (v2) with full support for all advanced and filtering options.

## Features
- Custom programmable search using Google CSE
- All new v2 parameters (sort, filter, gl, dateRestrict, SafeSearch strict)
- Full type safety for queries and responses
- Typed error classes for rich error handling
- API Key authentication handler; secure and pluggable

## Installation

```
npm install google-customsearch-sdk
```
## Usage

```typescript
import { GoogleCustomSearchClient } from 'google-customsearch-sdk';
const client = new GoogleCustomSearchClient('YOUR_API_KEY', 'YOUR_CSE_ID');
const result = await client.search({ q: 'OpenAI GPT-4' });
console.log(result.items[0].title, result.items[0].link);
```
## Types
- `ResultItem`
- `SearchInformation`
- `SearchResponse`

## API Error Classes
- `GoogleCustomSearchAPIError`
- `GoogleCustomSearchAuthError`

## License
Apache 2.0
