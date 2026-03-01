---
description: '# Using RPC'
---

# Using RPC

```
Turkchain supports Ethereum-compatible JSON-RPC methods.
```

### Curl Example

```
curl https://rpc.turkchain1919.com \
  -X POST \
  -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":1}'
```

```
This request returns the current network gas price.
```

### Supported RPC Methods

Commonly used methods:

* eth\_blockNumber
* eth\_getBalance
* eth\_getTransactionByHash
* eth\_sendRawTransaction
* eth\_call
* eth\_getLogs
