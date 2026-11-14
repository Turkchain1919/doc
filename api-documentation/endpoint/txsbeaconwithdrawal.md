# TurkScan® Consensus Withdrawal Data

Ethereum beacon withdrawals use chain-specific consensus semantics. An EVM transaction interface does not establish an equivalent withdrawal mechanism on Turkchain. No such Turkchain data service was established.

### TurkScan procedure

Use [API V2](../api-v2.md), the [Availability Inventory](../availability.md) and [Compatibility Matrix](../compatibility-matrix.md) to select a verified resource. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
