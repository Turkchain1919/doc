# TurkScan® Supported Network Configuration

This documentation targets Turkchain Mainnet only: decimal chain ID 1919, hex 0x77f, native TURK with 18 decimals, RPC https://rpc.turkscan.com and explorer https://turkscan.com. No multichain plan or hosted chainlist API is implied.

### TurkScan procedure

Use [Network Information](../../introduction/network-information.md) as the maintained configuration. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
