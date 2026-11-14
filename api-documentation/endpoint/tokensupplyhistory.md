# TurkScan® Historical Token Supply

Current token supply is supported, but arbitrary-height supply requires historical eth_call state or a separately maintained index. Handle archive-state unavailability and token-specific mint/burn behavior.

### TurkScan procedure

Use [Token API](../tokens-api.md) for verified current values and [RPC Integration](../../developers/rpc-integration.md) for node-state reads. No successful response is invented for an unverified service. Document the measurement or chain-specific mechanism before presenting it as a live feature.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).

## Additional verified RPC request

This read was exercised on 14 November 2026. It returned a JSON-RPC result. Historical reads prove availability for the sampled block, not every past block.

**Method:** POST. **URL:** `https://rpc.turkscan.com`. **Required:** `jsonrpc`, `id`, `method` and the exact method-specific `params` below. For logs, `topics` is an ordered topic filter; for historical reads the final block quantity selects the sampled state.

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":"0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271","data":"0x18160ddd"},"0x2f91a3"]}'
```

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x00000000000000000000000000000000000000000000d3c21bcecceda1000000"
}
```

Handle invalid filter arguments, missing historical state and JSON-RPC errors explicitly. Use bounded log ranges and never treat an empty result as failed execution.
