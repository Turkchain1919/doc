# Transactions API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/internal-transactions`

Read execution trace records.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/internal-transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `transaction_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `include_zero_value` | query | no | boolean |
| `items_count` | query | no | integer; min 1 |
| `index` | query | no | integer |
| `block_number` | query | no | integer; min 0 |
| `transaction_index` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/internal-transactions'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "block_number": 2604265,
      "created_contract": {
        "ens_domain_name": null,
        "hash": "0x98aeecA4A7e4D0801Ccd2F69ae26D2Ae31bd0C15",
        "implementations": [],
        "is_contract": true,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "error": null,
      "from": {
        "ens_domain_name": null,
        "hash": "0xb49B53f2d258a17E0fcC9d97ad2b93CB3eF65dBD",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "gas_limit": "1733110",
      "index": 0,
      "success": true,
      "timestamp": "2026-10-12T22:11:07.000000Z",
      "to": null,
      "transaction_hash": "0x4a62256c9e5e1e341ebae317fc461370d43e0387a2372e33aa93bd4fc7b0b1cd",
      "transaction_index": 0,
      "type": "create",
      "value": "0"
    }
  ],
  "meta": {
    "message": null,
    "status": 1
  },
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/main-page/transactions`

Read explorer homepage data — transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/main-page/transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/main-page/transactions'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
[
  {
    "has_error_in_internal_transactions": null,
    "block_number": 3117475,
    "exchange_rate": null,
    "transaction_types": [
      "contract_call"
    ],
    "historic_exchange_rate": null,
    "nonce": 2,
    "timestamp": "2026-11-12T21:19:21.000000Z",
    "base_fee_per_gas": "1000000000",
    "token_transfers": null,
    "fhe_operations_count": 0,
    "decoded_input": null,
    "gas_price": "1000100000",
    "gas_limit": "260611",
    "fee": {
      "type": "actual",
      "value": "175482546500000"
    },
    "method": "0x7c39d130",
    "authorization_list": [],
    "to": {
      "ens_domain_name": null,
      "hash": "0x5a1a042619AAE32c5282dB94769f78DF93AEeE6d",
      "implementations": [
        {
          "address_hash": "0x648C7F1bBef585b36bc1f21Fc28e60fa27935545",
          "name": null
        }
      ],
      "is_contract": true,
      "is_scam": false,
      "is_verified": false,
      "metadata": {
        "reputation": null,
        "tags": []
      },
      "name": null,
      "private_tags": [],
      "proxy_type": "eip1967",
      "public_tags": [],
      "reputation": "ok",
      "watchlist_names": []
    },
    "status": "ok",
    "gas_used": "175465",
    "from": {
      "ens_domain_name": null,
      "hash": "0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B",
      "implementations": [],
      "is_contract": false,
      "is_scam": false,
      "is_verified": false,
      "metadata": {
        "reputation": null,
        "tags": []
      },
      "name": null,
      "private_tags": [],
      "proxy_type": null,
      "public_tags": [],
      "reputation": "ok",
      "watchlist_names": []
    },
    "value": "0",
    "created_contract": null,
    "transaction_tag": null,
    "max_priority_fee_per_gas": "100000",
    "position": 0,
    "confirmations": 24532,
    "token_transfers_overflow": null,
    "type": 2,
    "transaction_burnt_fee": "175465000000000",
    "confirmation_duration": [
      0
    ],
    "revert_reason": null,
    "max_fee_per_gas": "2000100000",
    "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
    "result": "success",
    "is_pending_update": false,
    "raw_input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
    "priority_fee": "17546500000"
  }
]
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions`

Read indexed transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `filter` | query | no | string: `validated`, `pending` |
| `type` | query | no | string: `blob_transaction` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |
| `index` | query | no | integer |
| `hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `inserted_at` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "has_error_in_internal_transactions": null,
      "block_number": 3117475,
      "exchange_rate": null,
      "transaction_types": [
        "contract_call"
      ],
      "historic_exchange_rate": null,
      "nonce": 2,
      "timestamp": "2026-11-12T21:19:21.000000Z",
      "base_fee_per_gas": "1000000000",
      "token_transfers": null,
      "fhe_operations_count": 0,
      "decoded_input": null,
      "gas_price": "1000100000",
      "gas_limit": "260611",
      "fee": {
        "type": "actual",
        "value": "175482546500000"
      },
      "method": "0x7c39d130",
      "authorization_list": [],
      "to": {
        "ens_domain_name": null,
        "hash": "0x5a1a042619AAE32c5282dB94769f78DF93AEeE6d",
        "implementations": [
          {
            "address_hash": "0x648C7F1bBef585b36bc1f21Fc28e60fa27935545",
            "name": null
          }
        ],
        "is_contract": true,
        "is_scam": false,
        "is_verified": false,
        "metadata": {
          "reputation": null,
          "tags": []
        },
        "name": null,
        "private_tags": [],
        "proxy_type": "eip1967",
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "status": "ok",
      "gas_used": "175465",
      "from": {
        "ens_domain_name": null,
        "hash": "0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": {
          "reputation": null,
          "tags": []
        },
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "value": "0",
      "created_contract": null,
      "transaction_tag": null,
      "max_priority_fee_per_gas": "100000",
      "position": 0,
      "confirmations": 24533,
      "token_transfers_overflow": null,
      "type": 2,
      "transaction_burnt_fee": "175465000000000",
      "confirmation_duration": [
        0
      ],
      "revert_reason": null,
      "max_fee_per_gas": "2000100000",
      "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "result": "success",
      "is_pending_update": false,
      "raw_input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
      "priority_fee": "17546500000"
    }
  ],
  "next_page_params": {
    "index": 0,
    "block_number": 2948806
  }
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/stats`

Read indexed transactions — stats.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/stats`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| — | — | — | No parameters declared |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/stats'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "pending_transactions_count": "0",
  "transaction_fees_avg_24h": "0",
  "transaction_fees_sum_24h": "0",
  "transactions_count_24h": "0"
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}`

Read indexed transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "has_error_in_internal_transactions": null,
  "block_number": 3117475,
  "exchange_rate": null,
  "transaction_types": [
    "contract_call"
  ],
  "historic_exchange_rate": null,
  "nonce": 2,
  "timestamp": "2026-11-12T21:19:21.000000Z",
  "base_fee_per_gas": "1000000000",
  "token_transfers": [
    {
      "block_hash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
      "block_number": 3117475,
      "from": {
        "ens_domain_name": null,
        "hash": "0x0000000000000000000000000000000000000000",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "log_index": 3,
      "method": null,
      "timestamp": null,
      "to": {
        "ens_domain_name": null,
        "hash": "0xcf441f3199a5BA409CE6DD38E0eA630DD66A3918",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "token": {
        "address_hash": "0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f",
        "circulating_market_cap": null,
        "circulating_supply": null,
        "decimals": "18",
        "exchange_rate": null,
        "holders_count": "2",
        "icon_url": "https://raw.githubusercontent.com/Turkchain1919/Frontend/main/svg/ethereum.svg",
        "name": "Ethereum",
        "new_ui_multiplier": null,
        "reputation": "ok",
        "symbol": "ETH",
        "total_supply": "500000044000000000000",
        "type": "ERC-20",
        "ui_multiplier": null,
        "ui_multiplier_effective_at": null,
        "volume_24h": null
      },
      "token_type": "ERC-20",
      "total": {
        "decimals": "18",
        "ui_multiplier": null,
        "value": "44000000000000"
      },
      "transaction_hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "type": "token_minting"
    }
  ],
  "fhe_operations_count": 0,
  "decoded_input": {
    "method_call": "process(bytes arg0, bytes arg1)",
    "method_id": "7c39d130",
    "parameters": [
      {
        "name": "arg0",
        "type": "bytes",
        "value": "0x00000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b"
      }
    ]
  },
  "gas_price": "1000100000",
  "gas_limit": "260611",
  "fee": {
    "type": "actual",
    "value": "175482546500000"
  },
  "method": "process",
  "authorization_list": [],
  "to": {
    "ens_domain_name": null,
    "hash": "0x5a1a042619AAE32c5282dB94769f78DF93AEeE6d",
    "implementations": [
      {
        "address_hash": "0x648C7F1bBef585b36bc1f21Fc28e60fa27935545",
        "name": null
      }
    ],
    "is_contract": true,
    "is_scam": false,
    "is_verified": false,
    "metadata": null,
    "name": null,
    "private_tags": [],
    "proxy_type": "eip1967",
    "public_tags": [],
    "reputation": "ok",
    "watchlist_names": []
  },
  "status": "ok",
  "gas_used": "175465",
  "from": {
    "ens_domain_name": null,
    "hash": "0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B",
    "implementations": [],
    "is_contract": false,
    "is_scam": false,
    "is_verified": false,
    "metadata": null,
    "name": null,
    "private_tags": [],
    "proxy_type": null,
    "public_tags": [],
    "reputation": "ok",
    "watchlist_names": []
  },
  "value": "0",
  "created_contract": null,
  "transaction_tag": null,
  "max_priority_fee_per_gas": "100000",
  "position": 0,
  "confirmations": 24532,
  "token_transfers_overflow": false,
  "type": 2,
  "transaction_burnt_fee": "175465000000000",
  "confirmation_duration": [
    0
  ],
  "revert_reason": null,
  "max_fee_per_gas": "2000100000",
  "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
  "result": "success",
  "is_pending_update": false,
  "raw_input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
  "priority_fee": "17546500000"
}
```

### Response schema and errors

* HTTP `200` — schema `TransactionResponse`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/external-transactions`

Read indexed transactions — external-transactions.

**Observed:** HTTP 404 on 14 November 2026. This probe did not succeed. Do not treat this operation as an available feature without resolving the reported condition.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/external-transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/external-transactions'
```

### Observed response

HTTP 404. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "message": "Endpoint not available for current chain type"
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

The captured failure is the evidence for this request. Check feature configuration and required filters before depending on this route. Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/internal-transactions`

Read indexed transactions — internal-transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/internal-transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `include_zero_value` | query | no | boolean |
| `items_count` | query | no | integer; min 1 |
| `index` | query | no | integer |
| `block_number` | query | no | integer; min 0 |
| `transaction_index` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/internal-transactions'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [],
  "meta": {
    "message": "Some internal transactions within this block range have not yet been processed",
    "status": 2
  },
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/preview`

Read indexed transactions — preview.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/preview`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `preload_ens` | query | no | boolean |
| `preload_metadata` | query | no | boolean |
| `decode_input` | query | no | boolean |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/preview'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "from": {
    "ens_domain_name": null,
    "hash": "0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B",
    "metadata": null,
    "name": null
  },
  "method": "0x7c39d130",
  "status": "ok",
  "timestamp": "2026-11-12T21:19:21.000000Z",
  "to": {
    "ens_domain_name": null,
    "hash": "0x5a1a042619AAE32c5282dB94769f78DF93AEeE6d",
    "metadata": null,
    "name": null
  }
}
```

### Response schema and errors

* HTTP `200` — schema `TransactionPreview`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/raw-trace`

Read indexed transactions — raw-trace.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/raw-trace`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/raw-trace'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "calls": [
    {
      "calls": [
        {
          "calls": [
            {
              "from": "0xbf9569b06bcb6ccf776302b0697c79b8407d8e3f",
              "gas": "0x31d1d",
              "gasUsed": "0x98a",
              "input": "0xde523cf3",
              "output": "0x000000000000000000000000de841d6e6eb20ce112248e1f1ead665e491a7231",
              "to": "0xb747f4645a9bb5d580dd199f8cfa054a3f1b9655",
              "type": "DELEGATECALL",
              "value": "0x0"
            }
          ],
          "from": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
          "gas": "0x3457b",
          "gasUsed": "0x256a",
          "input": "0xde523cf3",
          "output": "0x000000000000000000000000de841d6e6eb20ce112248e1f1ead665e491a7231",
          "to": "0xbf9569b06bcb6ccf776302b0697c79b8407d8e3f",
          "type": "STATICCALL"
        }
      ],
      "from": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
      "gas": "0x36dd0",
      "gasUsed": "0x239f1",
      "input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
      "to": "0x648c7f1bbef585b36bc1f21fc28e60fa27935545",
      "type": "DELEGATECALL",
      "value": "0x0"
    }
  ],
  "from": "0x5b491b52ef948f9a60d75d2a56235fbfb8644f0b",
  "gas": "0x3fa03",
  "gasUsed": "0x2ad69",
  "input": "0x7c39d13000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000008500000000000000000000000048e6c30b97748d1e2e03bf3e9fbe3890ca5f8cca45b53a10a21290c68fbc150ab5090030f492ca1c640bb7ad9851cac2ca2dca3f0004e313f14593fc2644c32d3582c10831e717a44d39df6caaf929b8527597ee2b827cfd3981b0289087edc6556504ec88b8b0bfeee58e2f3f03791cba5cb25f04d55b271b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008d030004e9c700000001000000000000000000000000d13d97c537620ed5762343b78534c7581ed3a2fc0000077f000000000000000000000000 [excerpt]",
  "to": "0x5a1a042619aae32c5282db94769f78df93aeee6d",
  "type": "CALL",
  "value": "0x0"
}
```

### Response schema and errors

* HTTP `200` — schema `RawTrace`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/state-changes`

Read indexed transactions — state-changes.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/state-changes`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `items_count` | query | no | integer; min 1 |
| `state_changes_count` | query | no | integer; min 0 |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/state-changes'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "address": {
        "ens_domain_name": null,
        "hash": "0xb49B53f2d258a17E0fcC9d97ad2b93CB3eF65dBD",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "balance_after": "9.999769865572905796165017555E+28",
      "balance_before": "99997698655729057944103675546",
      "change": "17546500004",
      "is_miner": true,
      "token": null,
      "token_id": null,
      "type": "coin",
      "ui_multiplier": null
    }
  ],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/summary`

Read indexed transactions — summary.

**Observed:** HTTP 403 on 14 November 2026. This probe did not succeed. Do not treat this operation as an available feature without resolving the reported condition.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/summary`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `just_request_body` | query | no | boolean |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/summary'
```

### Observed response

HTTP 403. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "message": "Transaction Interpretation Service is disabled"
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

The captured failure is the evidence for this request. Check feature configuration and required filters before depending on this route. Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/transactions/{transaction_hash_param}/token-transfers`

Read indexed transactions — token-transfers.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/token-transfers`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `transaction_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `type` | query | no | value |
| `items_count` | query | no | integer; min 1 |
| `index` | query | no | integer |
| `block_number` | query | no | integer; min 0 |
| `batch_log_index` | query | no | integer |
| `batch_block_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `batch_transaction_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `index_in_batch` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/transactions/0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4/token-transfers'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "block_hash": "0x4fd75bbbd44cc6423f86e01f002ee47c4902e51dff0d160c49af78b62f109a89",
      "block_number": 3117475,
      "from": {
        "ens_domain_name": null,
        "hash": "0x0000000000000000000000000000000000000000",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "log_index": 3,
      "method": null,
      "timestamp": null,
      "to": {
        "ens_domain_name": null,
        "hash": "0xcf441f3199a5BA409CE6DD38E0eA630DD66A3918",
        "implementations": [],
        "is_contract": false,
        "is_scam": false,
        "is_verified": false,
        "metadata": null,
        "name": null,
        "private_tags": [],
        "proxy_type": null,
        "public_tags": [],
        "reputation": "ok",
        "watchlist_names": []
      },
      "token": {
        "address_hash": "0xBf9569B06bCb6ccF776302b0697c79B8407d8e3f",
        "circulating_market_cap": null,
        "circulating_supply": null,
        "decimals": "18",
        "exchange_rate": null,
        "holders_count": "2",
        "icon_url": "https://raw.githubusercontent.com/Turkchain1919/Frontend/main/svg/ethereum.svg",
        "name": "Ethereum",
        "new_ui_multiplier": null,
        "reputation": "ok",
        "symbol": "ETH",
        "total_supply": "500000044000000000000",
        "type": "ERC-20",
        "ui_multiplier": null,
        "ui_multiplier_effective_at": null,
        "volume_24h": null
      },
      "token_type": "ERC-20",
      "total": {
        "decimals": "18",
        "ui_multiplier": null,
        "value": "44000000000000"
      },
      "transaction_hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "type": "token_minting"
    }
  ],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
