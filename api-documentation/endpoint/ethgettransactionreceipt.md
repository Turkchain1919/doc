# TurkScan® eth_getTransactionReceipt

**Method:** HTTP POST. **URL:** `https://rpc.turkscan.com`. **JSON-RPC method:** `eth_getTransactionReceipt`.

### Parameters and required fields

`jsonrpc` must be `"2.0"`; supply an `id`, the exact `method` and the method-specific `params` array. This tested request uses 1 parameter(s). Address values are full 20-byte EVM identifiers, hashes are 32 bytes, and numeric block/index quantities are hexadecimal. `latest` selects the node's current state where accepted.

### Tested request

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_getTransactionReceipt","params":["0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4"]}'
```

### Captured response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "blockHash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
    "blockNumber": "0x2f91a3",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2ad69",
    "effectiveGasPrice": "0x3b9c50a0",
    "from": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
    "gasUsed": "0x2ad69",
    "logs": [
      {
        "address": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
        "topics": [
          "0x0d381c2a574ae8f04e213db7cfb4df8df712cdbd427d9868ffef380660ca6574"
        ],
        "data": "0x",
        "blockNumber": "0x2f91a3",
        "transactionHash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
        "transactionIndex": "0x0",
        "blockHash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
        "blockTimestamp": "0x6af62d59",
        "logIndex": "0x0",
        "removed": false
      }
    ],
    "logsBloom": "0x000080040000020000000000000000000000000010000010000000000000000000008020000000100000000000000000002000000000000000000000000400000000000000000000010000081000000080000000802400000000000000000000000004000200000000000000000008000000000000000000000000100000000000000000010000000000000000000000000000800000000000000000000000000000000040200000000001000000000000000000000000040000000000000080000000020000000000000000000000000000000000000200001000000000e000 [excerpt]",
    "status": "0x1",
    "to": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
    "transactionHash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
    "transactionIndex": "0x0",
    "type": "0x2"
  }
}
```

### Errors and usage

Inspect the JSON-RPC `error` object even on HTTP 200. Invalid arguments, unknown hashes and missing historical state need distinct handling. The [full read-only capture](../../reference/rpc-evidence.json) retains the original response; long values above may be excerpted. The explorer's module=proxy request returned Unknown module, so this page uses the actual network RPC instead. No signing key is required for this read.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
