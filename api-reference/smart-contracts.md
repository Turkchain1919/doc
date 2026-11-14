# Smart Contracts API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/config/smart-contracts/languages`

Read deployment configuration — smart-contracts, languages.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/config/smart-contracts/languages`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/config/smart-contracts/languages'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "languages": [
    "solidity"
  ]
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/smart-contracts/`

Read contract source records.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/smart-contracts/`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `sort` | query | no | string: `balance`, `transactions_count` |
| `order` | query | no | string: `asc`, `desc` |
| `q` | query | no | string |
| `filter` | query | no | string: `solidity`, `vyper`, `yul`, `geas` |
| `items_count` | query | no | integer; min 1 |
| `smart_contract_id` | query | no | integer |
| `coin_balance` | query | no | value |
| `hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `transactions_count` | query | no | value |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/smart-contracts/'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "address": {
        "ens_domain_name": null,
        "hash": "0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f",
        "implementations": [
          {
            "address_hash": "0xB747f4645A9bb5D580dd199f8cFa054A3f1b9655",
            "name": null
          }
        ],
        "is_contract": true,
        "is_scam": false,
        "is_verified": true,
        "metadata": null,
        "name": "TransparentUpgradeableProxy",
        "private_tags": [],
        "proxy_type": "eip1967",
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "certified": false,
      "coin_balance": "0",
      "compiler_version": "v0.8.28+commit.7893614a",
      "has_constructor_args": true,
      "language": "solidity",
      "license_type": "none",
      "market_cap": null,
      "optimization_enabled": true,
      "reputation": "ok",
      "transactions_count": 6,
      "verified_at": "2026-11-03T22:20:20.856948Z"
    }
  ],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/smart-contracts/counters`

Read contract source records — counters.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/smart-contracts/counters`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/smart-contracts/counters'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "smart_contracts": "115",
  "new_smart_contracts_24h": "16",
  "new_verified_smart_contracts_24h": "0",
  "verified_smart_contracts": "2"
}
```

### Response schema and errors

* HTTP `200` — schema `SmartContractCounters`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/smart-contracts/{address_hash_param}`

Read contract source records.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/smart-contracts/0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/smart-contracts/0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "constructor_args": "0x000000000000000000000000c7743c0d23a46ade301e3f0086c08de55653d36d000000000000000000000000db32dc96f68c5f48aba4d0decfa489f6eede1c9b00000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000144e80a7c7900000000000000000000000000000000000000000000001b1ae4d6e2ef50000000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001000000000000000000000000001ad4aea7240ea973963e965d63f91b2825d11b76000000000000000000000000de841d6e6eb20ce112248e1f1ead665e491a7231000000000000000000000000b3a776bfc1ba98ec9255e091aafe3aeb76d48c6b00000000000000000000000000000000000000000000000000 [excerpt]",
  "is_partially_verified": false,
  "is_changed_bytecode": false,
  "abi": [
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_logic",
          "type": "address"
        }
      ],
      "stateMutability": "payable",
      "type": "constructor"
    }
  ],
  "conflicting_implementations": null,
  "certified": false,
  "additional_sources": [],
  "is_verified_via_sourcify": false,
  "can_be_visualized_via_sol2uml": true,
  "evm_version": "paris",
  "language": "solidity",
  "is_verified_via_eth_bytecode_db": false,
  "is_fully_verified": true,
  "license_type": "none",
  "is_blueprint": false,
  "name": "TransparentUpgradeableProxy",
  "creation_bytecode": "0x6080604052604051610e03380380610e03833981016040819052610022916103f4565b828161003082826000610044565b5061003c905082610070565b505050610519565b61004d836100de565b60008251118061005a5750805b1561006b57610069838361011e565b505b505050565b7f7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f6100b0600080516020610dbc833981519152546001600160a01b031690565b604080516001600160a01b03928316815291841660208301520160405180910390a16100db8161014a565b50565b6100e7816101e6565b6040516001600160a01b038216907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a250565b60606101438383604051806060016040528060278152602001610ddc6027913961027a565b9392505050565b6001600160a01b0381166101b45760405162 [excerpt]",
  "external_libraries": [],
  "proxy_type": "eip1967",
  "implementations": [
    {
      "address_hash": "0xB747f4645A9bb5D580dd199f8cFa054A3f1b9655",
      "name": null
    }
  ],
  "verified_at": "2026-11-03T22:20:20.856948Z",
  "is_verified_via_verifier_alliance": false,
  "compiler_version": "v0.8.28+commit.7893614a",
  "decoded_constructor_args": [
    [
      "0xc7743C0D23A46AdE301E3f0086c08dE55653D36d"
    ]
  ],
  "sourcify_repo_url": null,
  "optimization_runs": 200,
  "compiler_settings": {
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
  "is_verified": true,
  "verified_twin_address_hash": null,
  "optimization_enabled": true,
  "deployed_bytecode": "0x60806040523661001357610011610017565b005b6100115b61001f610169565b6001600160a01b0316330361015f5760606001600160e01b0319600035166364d3180d60e11b810161005a5761005361019c565b9150610157565b63587086bd60e11b6001600160e01b031982160161007a576100536101f3565b63070d7c6960e41b6001600160e01b031982160161009a57610053610239565b621eb96f60e61b6001600160e01b03198216016100b95761005361026a565b63a39f25e560e01b6001600160e01b03198216016100d9576100536102aa565b60405162461bcd60e51b815260206004820152604260248201527f5472616e73706172656e745570677261646561626c6550726f78793a2061646d60448201527f696e2063616e6e6f742066616c6c6261636b20746f2070726f78792074617267606482015261195d60f21b608482015260a4015b60405180910390fd5b8151602083 [excerpt]",
  "source_code": "// SPDX-License-Identifier: MIT AND Apache-2.0\n// Flattened packaging only. Original source units and licenses are preserved in ../sources.\n// Hyperlane commit f556e18c9da88ce3d51a24164f22a7f27eb539fd; OpenZeppelin 4.9.3.\npragma solidity ^0.8.28;\n// Original source unit: @openzeppelin/contracts/proxy/Proxy.sol\n\n// OpenZeppelin Contracts (last updated v4.6.0) (proxy/Proxy.sol)\n\n\n\n/**\n * @dev This abstract contract provides a fallback function that delegates all calls to another contract using the EVM\n * instruction `delegatecall`. We refer to the second contract as the _implementation_ behind the proxy, and it has to\n * be specified by overriding the virtual {_implementation} function.\n *\n *  [excerpt]",
  "creation_status": "success",
  "file_path": "Turkchain-ETH-Remix/TransparentUpgradeableProxy.flat.sol"
}
```

### Response schema and errors

* HTTP `200` — schema `SmartContract`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/smart-contracts/{address_hash_param}/audit-reports`

Read contract source records — audit-reports.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/smart-contracts/0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f/audit-reports`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/smart-contracts/0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f/audit-reports'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
