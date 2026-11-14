# TurkScan® Native Supply Observations

**Method:** GET. **URL:** `https://turkscan.com/api?module=stats&action=ethsupply`

**Purpose:** Read available statistics.

**Parameters and required fields:** `module=stats` and `action=ethsupply` are required. No resource identifier required. Observations varied; no validated native monetary-supply methodology is established.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=stats&action=ethsupply'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "99997698806159833498634467085",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
