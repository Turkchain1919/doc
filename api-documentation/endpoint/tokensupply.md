# TurkScan® Token Total Supply

**Method:** GET. **URL:** `https://turkscan.com/api?module=stats&action=tokensupply&contractaddress=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271`

**Purpose:** Read available statistics.

**Parameters and required fields:** `module=stats` and `action=tokensupply` are required. Required: `contractaddress`. Token base units follow the token decimals.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=stats&action=tokensupply&contractaddress=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "1000000000000000000000000",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
