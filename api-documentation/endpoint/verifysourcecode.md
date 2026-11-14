# TurkScan® Submit Solidity Source

Submit exact Solidity compiler inputs and preserve the asynchronous job identifier. A queue acceptance is not a source match.

Read [Contract Verification API](../contract-verification-api.md) for source-confirmed routes, required compiler inputs, example publication requests, acceptance semantics and error cases. Read [Smart Contracts API](../smart-contracts-api.md) to inspect the actual published result.

No verification request, deployment or ownership signature was submitted during this audit. The distinction preserves on-chain and publication state while documenting the real workflow.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
