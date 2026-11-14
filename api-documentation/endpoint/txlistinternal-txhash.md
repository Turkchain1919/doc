# TurkScan® Internal Calls by Transaction

The parent transaction hash scopes the trace view. Internal calls are not separately signed transactions, and reverted subcalls need careful interpretation.

**Verified counterpart:** GET `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/internal-transactions`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/internal-transactions'
```

```json
{
  "items": [],
  "meta": {
    "message": "Some internal transactions within this block range have not yet been processed",
    "status": 2
  },
  "next_page_params": null
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
