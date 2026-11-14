# TurkScan® eth_getBlockTransactionCountByNumber

**Method:** HTTP POST. **URL:** `https://rpc.turkscan.com`. **JSON-RPC method:** `eth_getBlockTransactionCountByNumber`.

### Parameters and required fields

`jsonrpc` must be `"2.0"`; supply an `id`, the exact `method` and the method-specific `params` array. This tested request uses 1 parameter(s). Address values are full 20-byte EVM identifiers, hashes are 32 bytes, and numeric block/index quantities are hexadecimal. `latest` selects the node's current state where accepted.

### Tested request

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_getBlockTransactionCountByNumber","params":["0x2ff16b"]}'
```

### Captured response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x0"
}
```

### Errors and usage

Inspect the JSON-RPC `error` object even on HTTP 200. Invalid arguments, unknown hashes and missing historical state need distinct handling. The [full read-only capture](../reference/rpc-evidence.json) retains the original response; long values above may be excerpted. The explorer's module=proxy request returned Unknown module, so this page uses the actual network RPC instead. No signing key is required for this read.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
