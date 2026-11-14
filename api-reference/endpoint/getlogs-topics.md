# TurkScan® Event Logs by Topics

This topic requires deployment-specific evidence beyond the basic EVM interface. No successful dedicated TurkScan endpoint was established by the current audit.

### TurkScan procedure

Use [API V2](../api-v2.md), the [Availability Inventory](../availability.md) and [Compatibility Matrix](../compatibility-matrix.md) to select a verified resource. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).

## Additional verified RPC request

This read was exercised on 14 November 2026. It returned a JSON-RPC result. Historical reads prove availability for the sampled block, not every past block.

**Method:** POST. **URL:** `https://rpc.turkscan.com`. **Required:** `jsonrpc`, `id`, `method` and the exact method-specific `params` below. For logs, `topics` is an ordered topic filter; for historical reads the final block quantity selects the sampled state.

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_getLogs","params":[{"fromBlock":"0x2ff2e0","toBlock":"0x2ff2ea","topics":["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"]}]}'
```

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": []
}
```

Handle invalid filter arguments, missing historical state and JSON-RPC errors explicitly. Use bounded log ranges and never treat an empty result as failed execution.
