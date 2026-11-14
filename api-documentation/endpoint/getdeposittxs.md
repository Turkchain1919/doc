# TurkScan® Bridge Deposit Tracking

A bridge deposit requires a verified asset route and source contract. Do not equate any incoming native transfer with a bridge deposit or a completed destination mint.

### TurkScan procedure

Use [Cross-Chain Status](../../cross-chain/overview.md) and [Transfer Tracking](../../cross-chain/transfer-tracking.md). Record the actual source hash, message identifier, route contracts and destination receipt. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
