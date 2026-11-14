# TurkScan® Module/Action API

This API is hosted by TurkScan® at `https://turkscan.com/api`. Etherscan-style module/action identifiers are retained for compatibility. TurkScan is not the Etherscan-hosted multichain API V2, and support is limited to verified operations.

The requests below were sent as read-only GET requests on 14 November 2026. Empty results, null prices and unsupported modules are shown as observed. No key is embedded in examples.

## account / balance

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=balance&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=balance` are required. Required: `address`; optional `tag` as supported by the action. Native balance is in base units.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=balance&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "9999473528358100000",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / balancemulti

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=balancemulti&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=balancemulti` are required. Required: comma-separated `address` values. Each returned entry contains its own address and native balance.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=balancemulti&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": [
    {
      "account": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
      "balance": "9999473528358100000",
      "stale": false
    }
  ],
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / getminedblocks

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=getminedblocks&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=getminedblocks` are required. Required: `address`; optional paging. A generic mining name is not a validator reward policy.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=getminedblocks&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No blocks found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / token1155tx

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=token1155tx&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=token1155tx` are required. Use an address and/or supported contract filter; preserve token IDs and quantities in returned events.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=token1155tx&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No token transfers found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / tokenbalance

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=tokenbalance&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B&contractaddress=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=tokenbalance` are required. Required: `address`, `contractaddress`; optional `tag`. Units follow token decimals.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=tokenbalance&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B&contractaddress=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "0",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / tokenlist

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=tokenlist&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=tokenlist` are required. Required: `address`. Returns indexed token holdings when present.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=tokenlist&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No tokens found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / tokennfttx

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=tokennfttx&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=tokennfttx` are required. Use an address and/or supported contract filter; block range and page/offset select transfer history.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=tokennfttx&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No token transfers found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / tokentx

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=tokentx&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=tokentx` are required. Required for this example: `address`; optional `contractaddress`, `startblock`, `endblock`, `page`, `offset`, `sort`.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=tokentx&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No token transfers found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / txlist

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=txlist&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=txlist` are required. Required: `address`. Optional `startblock`, `endblock`, `page`, `offset`, `sort` (`asc` or `desc`).

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=txlist&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": [
    {
      "blockHash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
      "blockNumber": "3117475",
      "confirmations": "24660",
      "contractAddress": "",
      "cumulativeGasUsed": "175465",
      "from": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
      "gas": "260611",
      "gasPrice": "1000100000",
      "gasUsed": "175465",
      "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
      "isError": "0",
      "methodId": "0x7c39d130",
      "nonce": "2",
      "timeStamp": "1794518361",
      "to": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
      "transactionIndex": "0",
      "txreceipt_status": "1",
      "value": "0"
    }
  ],
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## account / txlistinternal

**Method:** GET. **URL:** `https://turkscan.com/api?module=account&action=txlistinternal&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

**Purpose:** Read address activity or balances.

**Parameters and required fields:** `module=account` and `action=txlistinternal` are required. Supply `address` or the action-supported transaction/block selector. This example uses address. Optional block range and paging depend on selector.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=account&action=txlistinternal&address=0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No internal transactions found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## block / getblocknobytime

**Method:** GET. **URL:** `https://turkscan.com/api?module=block&action=getblocknobytime&blockno=3000000&timestamp=1794500000&closest=before`

**Purpose:** Read block-indexed data.

**Parameters and required fields:** `module=block` and `action=getblocknobytime` are required. Required: `timestamp` in Unix seconds and `closest` (`before` or `after`).

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=block&action=getblocknobytime&blockno=3000000&timestamp=1794500000&closest=before'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "blockNumber": "3113945"
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## block / getblockreward

**Method:** GET. **URL:** `https://turkscan.com/api?module=block&action=getblockreward&blockno=3000000&timestamp=1794500000&closest=before`

**Purpose:** Read block-indexed data.

**Parameters and required fields:** `module=block` and `action=getblockreward` are required. Required: `blockno`. Generic reward fields are not a verified issuance schedule.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=block&action=getblockreward&blockno=3000000&timestamp=1794500000&closest=before'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "blockMiner": "0xb49b53f2d258a17e0fcc9d97ad2b93cb3ef65dbd",
    "blockNumber": "3000000",
    "blockReward": "0",
    "timeStamp": 1793895663,
    "uncleInclusionReward": "0",
    "uncles": []
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## contract / getabi

**Method:** GET. **URL:** `https://turkscan.com/api?module=contract&action=getabi&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f`

**Purpose:** Read contract verification or deployment data.

**Parameters and required fields:** `module=contract` and `action=getabi` are required. Required: `address` of a verified contract. `result` is a JSON-encoded ABI string.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=contract&action=getabi&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_logic\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"admin_\",\"type\":\"address\"},{\"internalType\":\"bytes\",\"name\":\"_data\",\"type\":\"bytes\"}],\"stateMutability\":\"payable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"previousAdmin\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"newAdmin\",\"type\":\"address\"}],\"name\":\"AdminChanged\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"beacon\",\"type\":\"address\"}],\"name\":\"BeaconUpgraded\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"implementa [excerpt]",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## contract / getcontractcreation

**Method:** GET. **URL:** `https://turkscan.com/api?module=contract&action=getcontractcreation&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f`

**Purpose:** Read contract verification or deployment data.

**Parameters and required fields:** `module=contract` and `action=getcontractcreation` are required. Required: `contractaddresses` as a comma-separated list of contract addresses.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=contract&action=getcontractcreation&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": [
    {
      "blockNumber": "2970579",
      "contractAddress": "0xbf9569b06bcb6ccf776302b0697c79b8407d8e3f",
      "contractCreator": "0x8b00ecb1e8bf59f5ab4ba0f0c528c4f4d850280e",
      "contractFactory": "",
      "creationBytecode": "0x6080604052604051610e03380380610e03833981016040819052610022916103f4565b828161003082826000610044565b5061003c905082610070565b505050610519565b61004d836100de565b60008251118061005a5750805b1561006b57610069838361011e565b505b505050565b7f7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f6100b0600080516020610dbc833981519152546001600160a01b031690565b604080516001600160a01b03928316815291841660208301520160405180910390a16100db8161014a565b50565b6100e7816101e6565b6040516001600160a01b038216907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a250565b60606101438383604051806060016040528060278152602001610ddc6027913961027a565b9392505050565b6001600160a01b0381166101b45760405162 [excerpt]",
      "timestamp": "1793739669",
      "txHash": "0x1d9dba155e971db814e60f59e827b4d9fa98784dd6f3e29678d912ac18b62b8a"
    }
  ],
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## contract / getsourcecode

**Method:** GET. **URL:** `https://turkscan.com/api?module=contract&action=getsourcecode&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f`

**Purpose:** Read contract verification or deployment data.

**Parameters and required fields:** `module=contract` and `action=getsourcecode` are required. Required: `address`. Results can include compiler settings and source records.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=contract&action=getsourcecode&address=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f&contractaddresses=0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": [
    {
      "CompilerSettings": {
        "evmVersion": "paris",
        "libraries": {},
        "optimizer": {
          "enabled": true,
          "runs": 200
        },
        "outputSelection": {
          "*": {
            "": [
              "*"
            ],
            "*": [
              "*"
            ]
          }
        }
      },
      "ConstructorArguments": "0x000000000000000000000000c7743c0d23a46ade301e3f0086c08de55653d36d000000000000000000000000db32dc96f68c5f48aba4d0decfa489f6eede1c9b00000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000144e80a7c7900000000000000000000000000000000000000000000001b1ae4d6e2ef50000000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001000000000000000000000000001ad4aea7240ea973963e965d63f91b2825d11b76000000000000000000000000de841d6e6eb20ce112248e1f1ead665e491a7231000000000000000000000000b3a776bfc1ba98ec9255e091aafe3aeb76d48c6b00000000000000000000000000000000000000000000000000 [excerpt]",
      "OptimizationRuns": 200,
      "ImplementationAddress": "0xb747f4645a9bb5d580dd199f8cfa054a3f1b9655",
      "ImplementationAddresses": [
        "0xb747f4645a9bb5d580dd199f8cfa054a3f1b9655"
      ],
      "IsProxy": "true",
      "SourceCode": "// SPDX-License-Identifier: MIT AND Apache-2.0\n// Flattened packaging only. Original source units and licenses are preserved in ../sources.\n// Hyperlane commit f556e18c9da88ce3d51a24164f22a7f27eb539fd; OpenZeppelin 4.9.3.\npragma solidity ^0.8.28;\n// Original source unit: @openzeppelin/contracts/proxy/Proxy.sol\n\n// OpenZeppelin Contracts (last updated v4.6.0) (proxy/Proxy.sol)\n\n\n\n/**\n * @dev This abstract contract provides a fallback function that delegates all calls to another contract using the EVM\n * instruction `delegatecall`. We refer to the second contract as the _implementation_ behind the proxy, and it has to\n * be specified by overriding the virtual {_implementation} function.\n *\n *  [excerpt]",
      "ABI": "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_logic\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"admin_\",\"type\":\"address\"},{\"internalType\":\"bytes\",\"name\":\"_data\",\"type\":\"bytes\"}],\"stateMutability\":\"payable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"previousAdmin\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"newAdmin\",\"type\":\"address\"}],\"name\":\"AdminChanged\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"beacon\",\"type\":\"address\"}],\"name\":\"BeaconUpgraded\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"implementa [excerpt]",
      "ContractName": "TransparentUpgradeableProxy",
      "CompilerVersion": "v0.8.28+commit.7893614a",
      "OptimizationUsed": "true",
      "EVMVersion": "paris",
      "FileName": "Turkchain-ETH-Remix/TransparentUpgradeableProxy.flat.sol",
      "Address": "0xbf9569b06bcb6ccf776302b0697c79b8407d8e3f"
    }
  ],
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## gastracker / gasoracle

**Method:** GET. **URL:** `https://turkscan.com/api?module=gastracker&action=gasoracle`

**Purpose:** Check gas-oracle compatibility.

**Parameters and required fields:** `module=gastracker` and `action=gasoracle` are required. The gastracker module returned HTTP 400 Unknown module; use V2 stats for available estimates.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=gastracker&action=gasoracle'
```

### Observed response

HTTP 400. First array item only; long strings may be excerpted.

```json
{
  "message": "Unknown module",
  "result": null,
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## logs / getLogs

**Method:** GET. **URL:** `https://turkscan.com/api?module=logs&action=getLogs&fromBlock=3000000&toBlock=3117475&address=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271`

**Purpose:** Read indexed events.

**Parameters and required fields:** `module=logs` and `action=getLogs` are required. Required selectors include a bounded `fromBlock` and `toBlock`, plus an address or supported topic filter. Topic operators are action-specific.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=logs&action=getLogs&fromBlock=3000000&toBlock=3117475&address=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "No logs found",
  "result": [],
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## proxy / eth_blockNumber

**Method:** GET. **URL:** `https://turkscan.com/api?module=proxy&action=eth_blockNumber`

**Purpose:** Check node-proxy compatibility.

**Parameters and required fields:** `module=proxy` and `action=eth_blockNumber` are required. The proxy module returned HTTP 400 Unknown module; use network JSON-RPC instead.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=proxy&action=eth_blockNumber'
```

### Observed response

HTTP 400. First array item only; long strings may be excerpted.

```json
{
  "message": "Unknown module",
  "result": null,
  "status": "0"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## stats / coinprice

**Method:** GET. **URL:** `https://turkscan.com/api?module=stats&action=coinprice`

**Purpose:** Read available statistics.

**Parameters and required fields:** `module=stats` and `action=coinprice` are required. No resource identifier required. Null prices are unavailable, not zero.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=stats&action=coinprice'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "coin_btc": null,
    "coin_btc_timestamp": null,
    "coin_usd": null,
    "coin_usd_timestamp": null
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## stats / ethprice

**Method:** GET. **URL:** `https://turkscan.com/api?module=stats&action=ethprice`

**Purpose:** Read available statistics.

**Parameters and required fields:** `module=stats` and `action=ethprice` are required. No resource identifier required. Protocol fields retain their historic names; returned prices were null.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=stats&action=ethprice'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "ethbtc": null,
    "ethbtc_timestamp": null,
    "ethusd": null,
    "ethusd_timestamp": null
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## stats / ethsupply

**Method:** GET. **URL:** `https://turkscan.com/api?module=stats&action=ethsupply`

**Purpose:** Read available statistics.

**Parameters and required fields:** `module=stats` and `action=ethsupply` are required. No resource identifier required. Observations varied; no validated native monetary-supply methodology is established.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=stats&action=ethsupply'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "99997698806159833498634467085",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## stats / tokensupply

**Method:** GET. **URL:** `https://turkscan.com/api?module=stats&action=tokensupply&contractaddress=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271`

**Purpose:** Read available statistics.

**Parameters and required fields:** `module=stats` and `action=tokensupply` are required. Required: `contractaddress`. Token base units follow the token decimals.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=stats&action=tokensupply&contractaddress=0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": "1000000000000000000000000",
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## transaction / getstatus

**Method:** GET. **URL:** `https://turkscan.com/api?module=transaction&action=getstatus&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4`

**Purpose:** Read transaction execution information.

**Parameters and required fields:** `module=transaction` and `action=getstatus` are required. Required: `txhash`. Inspect `isError` and `errDescription` in the result.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=transaction&action=getstatus&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "errDescription": "",
    "isError": "0"
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## transaction / gettxinfo

**Method:** GET. **URL:** `https://turkscan.com/api?module=transaction&action=gettxinfo&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4`

**Purpose:** Read transaction execution information.

**Parameters and required fields:** `module=transaction` and `action=gettxinfo` are required. Required: `txhash`. Includes indexed transaction details.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=transaction&action=gettxinfo&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "blockNumber": "3117475",
    "confirmations": "24660",
    "from": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
    "gasLimit": "260611",
    "gasPrice": "1000100000",
    "gasUsed": "175465",
    "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
    "input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
    "logs": [
      {
        "address": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
        "data": "0x",
        "index": "0",
        "topics": [
          "0x0d381c2a574ae8f04e213db7cfb4df8df712cdbd427d9868ffef380660ca6574"
        ]
      }
    ],
    "next_page_params": null,
    "revertReason": "",
    "success": true,
    "timeStamp": "1794518361",
    "to": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
    "value": "0"
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).

## transaction / gettxreceiptstatus

**Method:** GET. **URL:** `https://turkscan.com/api?module=transaction&action=gettxreceiptstatus&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4`

**Purpose:** Read transaction execution information.

**Parameters and required fields:** `module=transaction` and `action=gettxreceiptstatus` are required. Required: `txhash`. Distinguish the envelope status from the receipt result status.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api?module=transaction&action=gettxreceiptstatus&txhash=0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4'
```

### Observed response

HTTP 200. First array item only; long strings may be excerpted.

```json
{
  "message": "OK",
  "result": {
    "status": "1"
  },
  "status": "1"
}
```

### Errors and usage

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](error-handling.md), [Rate Limits](rate-limits.md) and [complete captures](reference/endpoint-evidence.json).
