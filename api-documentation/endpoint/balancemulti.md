# TurkScan® Multiple Address Balances

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=balancemulti&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=balancemulti` are required. Required: comma-separated `address` values. Each returned entry contains its own address and native balance.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=balancemulti&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": [
    {
      "account": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
      "balance": "9999473528358100000",
      "stale": false
    }
  ],
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
