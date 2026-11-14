# TurkScan® Uncle-Block RPC Compatibility

The generic EVM tooling vocabulary includes uncle-block queries, but no applicable Turkchain uncle dataset was established. Do not report a hypothetical uncle as a canonical block.

### TurkScan procedure

Use [API V2](../api-v2.md), the [Availability Inventory](../availability.md) and [Compatibility Matrix](../compatibility-matrix.md) to select a verified resource. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
