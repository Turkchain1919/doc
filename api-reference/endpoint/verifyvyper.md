# TurkScan® Vyper Verification Configuration

The deployed source has Vyper submission routes, but enabled compiler and verifier choices must be checked through verification/config. This audit did not submit a Vyper job, so a successful match is not claimed.

### TurkScan procedure

Read the live `GET https://turkscan.com/api/v2/smart-contracts/verification/config` response before selecting a language or method. See [Verification API](../contract-verification.md). No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
