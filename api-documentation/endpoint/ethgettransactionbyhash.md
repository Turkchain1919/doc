# TurkScan® eth_getTransactionByHash

**Method:** HTTP POST. **URL:** `https://rpc.turkscan.com`. **JSON-RPC method:** `eth_getTransactionByHash`.

### Parameters and required fields

`jsonrpc` must be `"2.0"`; supply an `id`, the exact `method` and the method-specific `params` array. This tested request uses 1 parameter(s). Address values are full 20-byte EVM identifiers, hashes are 32 bytes, and numeric block/index quantities are hexadecimal. `latest` selects the node's current state where accepted.

### Tested request

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_getTransactionByHash","params":["0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4"]}'
```

### Captured response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "blockHash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
    "blockNumber": "0x2f91a3",
    "from": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
    "gas": "0x3fa03",
    "gasPrice": "0x3b9c50a0",
    "maxFeePerGas": "0x77371aa0",
    "maxPriorityFeePerGas": "0x186a0",
    "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
    "input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791c [excerpt]",
    "nonce": "0x2",
    "to": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
    "transactionIndex": "0x0",
    "value": "0x0",
    "type": "0x2",
    "accessList": [],
    "chainId": "0x77f",
    "v": "0x0",
    "r": "0x2b33dd3afff14e55e0005679d72bd187a1807194cd85f937c689deac287d0a74",
    "s": "0x44976c201f00a76bda1bc4d62b3a17faa0ee05a24d130570b03a7bacfec74def",
    "yParity": "0x0"
  }
}
```

### Errors and usage

Inspect the JSON-RPC `error` object even on HTTP 200. Invalid arguments, unknown hashes and missing historical state need distinct handling. The [full read-only capture](../../reference/rpc-evidence.json) retains the original response; long values above may be excerpted. The explorer's module=proxy request returned Unknown module, so this page uses the actual network RPC instead. No signing key is required for this read.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
