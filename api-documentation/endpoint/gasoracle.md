# TurkScan® Current Gas Estimates

**Method:** GET. **URL:** `https://turkscan.com/api?module=gastracker&action=gasoracle`

**Purpose:** Check gas-oracle compatibility.

**Parameters and required fields:** `module=gastracker` and `action=gasoracle` are required. The gastracker module returned HTTP 400 Unknown module; use V2 stats for available estimates.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=gastracker&action=gasoracle'
```

### Observed response

HTTP 400. First array item only; long strings may be excerpted.

```json
{
  "message": "Unknown module",
  "result": null,
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
