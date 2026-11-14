# TurkScan® Broadcast a Signed Transaction

eth_sendRawTransaction broadcasts a previously signed transaction through https://rpc.turkscan.com. It can spend real TURK and change contract state. Validate chain ID 1919, preserve the computed hash and reconcile receipts before retrying. No transaction was signed or broadcast in this audit; therefore no successful submission response is fabricated.

### TurkScan procedure

Use a wallet or signing library, verify the network, simulate the intended operation and obtain explicit user confirmation before broadcasting. See [First Transaction](https://doc.turkscan.com/getting-started/first-transaction). No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
