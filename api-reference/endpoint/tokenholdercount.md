# TurkScan® Token Holder Count

Use available token counters and token metadata holder counts. Indexing and token behavior can affect counts; do not equate holders with unique people.

**Verified counterpart:** GET `https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/counters`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/counters'
```

```json
{
  "transfers_count": "128889",
  "token_holders_count": "6",
  "ui_multiplier_changes_count": "0"
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
