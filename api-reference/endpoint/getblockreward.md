# TurkScan® Block Reward Fields

**Method:** GET. **URL:** `https://turkscan.com/api?module=block&action=getblockreward&blockno=3000000&timestamp=1794500000&closest=before`

**Purpose:** Read block-indexed data.

**Parameters and required fields:** `module=block` and `action=getblockreward` are required. Required: `blockno`. Generic reward fields are not a verified issuance schedule.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=block&action=getblockreward&blockno=3000000&timestamp=1794500000&closest=before'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "blockMiner": "0xb49b53f2d258a17e0fcc9d97ad2b93cb3ef65dbd",
    "blockNumber": "3000000",
    "blockReward": "0",
    "timeStamp": 1793895663,
    "uncleInclusionReward": "0",
    "uncles": []
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
