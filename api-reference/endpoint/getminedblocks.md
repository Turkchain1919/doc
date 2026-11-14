# TurkScan® Blocks Associated with an Address

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=getminedblocks&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=getminedblocks` are required. Required: `address`; optional paging. A generic mining name is not a validator reward policy.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=getminedblocks&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No blocks found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
