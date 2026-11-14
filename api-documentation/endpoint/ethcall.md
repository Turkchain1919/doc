# TurkScan® eth_call

**Method:** HTTP POST. **URL:** `https://rpc.turkscan.com`. **JSON-RPC method:** `eth_call`.

### Parameters and required fields

`jsonrpc` must be `"2.0"`; supply an `id`, the exact `method` and the method-specific `params` array. This tested request uses 2 parameter(s). Address values are full 20-byte EVM identifiers, hashes are 32 bytes, and numeric block/index quantities are hexadecimal. `latest` selects the node's current state where accepted.

### Tested request

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":"0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271","data":"0x18160ddd"},"latest"]}'
```

### Captured response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x00000000000000000000000000000000000000000000d3c21bcecceda1000000"
}
```

### Errors and usage

Inspect the JSON-RPC `error` object even on HTTP 200. Invalid arguments, unknown hashes and missing historical state need distinct handling. The [full read-only capture](../../reference/rpc-evidence.json) retains the original response; long values above may be excerpted. The explorer's module=proxy request returned Unknown module, so this page uses the actual network RPC instead. No signing key is required for this read.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
