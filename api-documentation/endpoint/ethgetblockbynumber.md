# TurkScan® eth_getBlockByNumber

**Method:** HTTP POST. **URL:** `https://rpc.turkscan.com`. **JSON-RPC method:** `eth_getBlockByNumber`.

### Parameters and required fields

`jsonrpc` must be `"2.0"`; supply an `id`, the exact `method` and the method-specific `params` array. This tested request uses 2 parameter(s). Address values are full 20-byte EVM identifiers, hashes are 32 bytes, and numeric block/index quantities are hexadecimal. `latest` selects the node's current state where accepted.

### Tested request

```bash
curl https://rpc.turkscan.com -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_getBlockByNumber","params":["0x2ff16b",false]}'
```

### Captured response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "baseFeePerGas": "0x3b9aca00",
    "blobGasUsed": "0x0",
    "difficulty": "0x0",
    "excessBlobGas": "0x0",
    "extraData": "0x",
    "gasLimit": "0xffffffff",
    "gasUsed": "0x0",
    "hash": "0xfe229c3c9869b286d63b1651bbc20da499c4f67d3a0924a61ab63f4e482c1326",
    "logsBloom": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 [excerpt]",
    "miner": "0xb49b53f2d258a17e0fcc9d97ad2b93cb3ef65dbd",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x2ff16b",
    "parentBeaconBlockRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "parentHash": "0xb9e3ee52488f7fcebae30e4ce3e9f12338e8bcb2e7b2f778ae36e93aeff8fe46",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "requestsHash": "0xe3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x26b",
    "stateRoot": "0x4929728c0589e1c22fb52689da42d6b0f0ac2d98fdecb24a394defc2a0242ca2",
    "timestamp": "0x6af82104",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": [],
    "withdrawals": [],
    "withdrawalsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421"
  }
}
```

### Errors and usage

Inspect the JSON-RPC `error` object even on HTTP 200. Invalid arguments, unknown hashes and missing historical state need distinct handling. The [full read-only capture](../../reference/rpc-evidence.json) retains the original response; long values above may be excerpted. The explorer's module=proxy request returned Unknown module, so this page uses the actual network RPC instead. No signing key is required for this read.

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
