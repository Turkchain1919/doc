# Using RPC

Send JSON-RPC requests with HTTP POST and `Content-Type: application/json`:

```bash
curl https://rpc.turkscan.com \
  -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_chainId","params":[]}'
```

```json
{"jsonrpc":"2.0","id":1,"result":"0x77f"}
```

Read methods such as `eth_blockNumber`, `eth_getBalance`, `eth_getCode` and `eth_getTransactionReceipt` inspect node state. `eth_call` simulates a call; it does not persist changes. `eth_sendRawTransaction` broadcasts a signed transaction and must not be treated as a read operation.

The explorer REST API is a different interface at `https://turkscan.com/api/v2`. See [RPC Integration](../developers/rpc-integration.md).
