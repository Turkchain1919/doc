# TurkScan® Bridge Transaction Research

Bridge events depend on the verified route, domains and contract ABI. No generic Plasma bridge was established on Turkchain. Track actual source dispatch and destination delivery using the route's protocol.

### TurkScan procedure

Use [Cross-Chain Status](https://doc.turkscan.com/cross-chain/overview) and [Transfer Tracking](https://doc.turkscan.com/cross-chain/transfer-tracking). Record the actual source hash, message identifier, route contracts and destination receipt. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
