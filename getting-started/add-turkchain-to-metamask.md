# Add Turkchain to MetaMask

```
# Add Turkchain to MetaMask
```

To manually add Turkchain to MetaMask:

1. Open MetaMask
2. Click "Add Network"
3. Choose "Add a network manually"
4. Enter the following details

|                    |                                                                |
| ------------------ | -------------------------------------------------------------- |
| RPC URL            | [https://rpc.turkchain1919.com](https://rpc.turkchain1919.com) |
| Chain ID           | 1919                                                           |
| Currency Symbol    | TURK                                                           |
| Block Explorer URL | [https://turkscan.com](https://turkscan.com)                   |

```
After saving, MetaMask will switch to Turkchain automatically.
```

## Using RPC

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

## First Transaction

To send a transaction on Turkchain:

1. Connect MetaMask to Turkchain
2. Ensure you have TURK balance
3. Enter recipient address
4. Set amount
5. Confirm transaction

### Transaction Lifecycle

Transaction flow:

User Wallet → RPC Node → Validator Set → Block Inclusion → Finality

### Explorer Tracking

After sending a transaction, copy the transaction hash and search it on:

https://turkscan.com
