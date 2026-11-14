# TurkScan® Historical Native Pricing

The market chart was reachable but can be empty. Do not invent a TURK price series or fill missing quotes with zero.

**Verified counterpart:** GET `https://turkscan.com/api/v2/stats/charts/market`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/stats/charts/market'
```

```json
{
  "available_supply": 0,
  "chart_data": []
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
