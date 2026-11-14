# TurkScan® Verified Contract Source

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

Inspect `status`, `message` and `result`, even on HTTP 200. `status: "0"` can accompany an empty result. Invalid selectors and unsupported modules must not be treated as successful data. These observations do not establish every optional selector or POST variant. See [Errors](../error-handling.md), [Rate Limits](../rate-limits.md) and [complete captures](../../reference/endpoint-evidence.json).

**Integration notes:** Keep native amounts in 18-decimal TURK base units, preserve large integer precision, distinguish null from zero and apply bounded retries to safe reads. See [errors](../error-handling.md) and [rate limits](../rate-limits.md).
