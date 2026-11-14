# TurkScan® Receipt Status

**Method:** GET. **URL:** `https://turkscan.com/api?module=transaction&action=gettxreceiptstatus&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4`

**Purpose:** Read transaction execution information.

**Parameters and required fields:** `module=transaction` and `action=gettxreceiptstatus` are required. Required: `txhash`. Distinguish the envelope status from the receipt result status.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=transaction&action=gettxreceiptstatus&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "status": "1"
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
