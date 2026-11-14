# TurkScan® Future Block Estimates

The tested V2 countdown request did not succeed for its sampled current block. A future-height estimate, when available, is only an estimate derived from observed block times and is not an execution guarantee.

### TurkScan procedure

Use [API V2](../api-v2.md), the [Availability Inventory](../availability.md) and [Compatibility Matrix](../compatibility-matrix.md) to select a verified resource. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).

## Verified future-height estimate

Both V2 and module/action countdown requests succeeded when the requested height was actually in the future. A mined/current-height request correctly returns an error. The values below are historical estimates, not a promise of future inclusion time.

**Method:** GET. **URL:** `https://turkscan.com/api/v2/blocks/3152501/countdown`. **Required:** the future block number in the path, or `module=block`, `action=getblockcountdown`, `blockno` in the compatibility query.

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks/3152501/countdown'
```

```json
{
  "countdown_block_number": "3152501",
  "current_block_number": "3142501",
  "estimated_time_in_seconds": "52530.0",
  "remaining_blocks_count": "10000"
}
```

**Method:** GET. **URL:** `https://turkscan.com/api?module=block&action=getblockcountdown&blockno=3152501`. **Required:** the future block number in the path, or `module=block`, `action=getblockcountdown`, `blockno` in the compatibility query.

```bash
curl --fail-with-body 'https://turkscan.com/api?module=block&action=getblockcountdown&blockno=3152501'
```

```json
{
  "message": "OK",
  "result": {
    "CountdownBlock": "3152501",
    "CurrentBlock": "3142501",
    "EstimateTimeInSec": "52530.0",
    "RemainingBlock": "10000"
  },
  "status": "1"
}
```
