# TurkScan® Historical Native Balance

Address balance history is indexed event history. It is not a guaranteed arbitrary-height archive query. For an exact past block, use eth_getBalance against a provider that retains that state and handle missing historical state.

**Verified counterpart:** GET `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/coin-balance-history`.

### Request and observed response

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/coin-balance-history'
```

```json
{
  "items": [
    {
      "block_number": 3117475,
      "block_timestamp": "2026-11-12T21:19:21Z",
      "delta": "-175482546500000",
      "transaction_hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "value": "9999473528358100000"
    }
  ],
  "next_page_params": null
}
```

The response is a 14 November 2026 snapshot. Lists retain the first item and long values may be excerpted. Use the [category reference](../api-v2.md) for all required path/query fields, response schemas, error cases and pagination. A resource alternative does not imply that an identically named module/action endpoint is exposed.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).

## Additional verified RPC request

This read was exercised on 14 November 2026. It returned a JSON-RPC result. Historical reads prove availability for the sampled block, not every past block.

**Method:** POST. **URL:** `https://rpc.turkscan.com`. **Required:** `jsonrpc`, `id`, `method` and the exact method-specific `params` below. For logs, `topics` is an ordered topic filter; for historical reads the final block quantity selects the sampled state.

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_getBalance","params":["0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B","0x2f91a3"]}'
```

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x8ac54431ceb4dc20"
}
```

Handle invalid filter arguments, missing historical state and JSON-RPC errors explicitly. Use bounded log ranges and never treat an empty result as failed execution.
