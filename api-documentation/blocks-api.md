# Blocks API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/blocks`

Read canonical indexed blocks.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/blocks`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `type` | query | no | string: `uncle`, `reorg`, `block` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "base_fee_per_gas": "1000000000",
      "burnt_fees": "0",
      "burnt_fees_percentage": null,
      "difficulty": "0",
      "gas_limit": "4294967295",
      "gas_target_percentage": -100.0,
      "gas_used": "0",
      "gas_used_percentage": 0.0,
      "hash": "0x5a45faca9a8c98fe652affa072a9827bb6c396a0ca478e4f7b1d51fb3415adc8",
      "height": 3142006,
      "internal_transactions_count": null,
      "is_pending_update": false,
      "miner": {
        "ens_domain_name": null,
        "hash": "0xb49B53f2d258a17E0fcC9d97ad2b93CB3eF65dBD",
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
      "nonce": "0x0000000000000000",
      "parent_hash": "0x971e406f94869dc2c7b013e657f1914474bb380818bc0318986bee8a2623a8b7",
      "priority_fee": "0",
      "rewards": [],
      "size": 619,
      "timestamp": "2026-11-14T08:52:13.000000Z",
      "total_difficulty": null,
      "transaction_fees": "0",
      "transactions_count": 0,
      "type": "block",
      "uncles_hashes": [],
      "withdrawals_count": null
    }
  ],
  "next_page_params": {
    "block_number": 3141957
  }
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/blocks/{block_hash_or_number_param}`

Read canonical indexed blocks.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/blocks/3141995`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `block_hash_or_number_param` | path | yes | value |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks/3141995'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "base_fee_per_gas": "1000000000",
  "burnt_fees": "0",
  "burnt_fees_percentage": null,
  "difficulty": "0",
  "gas_limit": "4294967295",
  "gas_target_percentage": -100.0,
  "gas_used": "0",
  "gas_used_percentage": 0.0,
  "hash": "0xfe229c3c9869b286d63b1651bbc20da499c4f67d3a0924a61ab63f4e482c1326",
  "height": 3141995,
  "internal_transactions_count": 0,
  "is_pending_update": false,
  "miner": {
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
  "nonce": "0x0000000000000000",
  "parent_hash": "0xb9e3ee52488f7fcebae30e4ce3e9f12338e8bcb2e7b2f778ae36e93aeff8fe46",
  "priority_fee": "0",
  "rewards": [],
  "size": 619,
  "timestamp": "2026-11-14T08:51:16.000000Z",
  "total_difficulty": null,
  "transaction_fees": "0",
  "transactions_count": 0,
  "type": "block",
  "uncles_hashes": [],
  "withdrawals_count": 0
}
```

### Response schema and errors

* HTTP `200` — schema `BlockResponse`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/blocks/{block_hash_or_number_param}/internal-transactions`

Read canonical indexed blocks — internal-transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/blocks/3141995/internal-transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `block_hash_or_number_param` | path | yes | value |
| `internal_type` | query | no | string: `call`, `create`, `create2`, `reward`, `selfdestruct`, `stop` |
| `call_type` | query | no | string: `call`, `callcode`, `delegatecall`, `staticcall` |
| `include_zero_value` | query | no | boolean |
| `items_count` | query | no | integer; min 1 |
| `transaction_index` | query | no | integer |
| `index` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks/3141995/internal-transactions'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [],
  "meta": {
    "message": null,
    "status": 1
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

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/blocks/{block_hash_or_number_param}/transactions`

Read canonical indexed blocks — transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/blocks/3141995/transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `block_hash_or_number_param` | path | yes | value |
| `type` | query | no | string: `coin_transfer`, `contract_call`, `contract_creation`, `token_transfer`, `token_creation` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |
| `index` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks/3141995/transactions'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/blocks/{block_number_param}/countdown`

Read canonical indexed blocks — countdown.

**Observed:** HTTP 404 on 14 November 2026. This probe did not succeed. Do not treat this operation as an available feature without resolving the reported condition.

**Exact tested URL:** `https://turkscan.com/api/v2/blocks/3141995/countdown`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `block_number_param` | path | yes | integer; min 0 |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/blocks/3141995/countdown'
```

### Observed response

HTTP 404. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "message": "Block number already mined"
}
```

### Response schema and errors

* HTTP `200` — schema `BlockCountdown`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.
* HTTP `501` — schema `NotImplementedResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

The captured failure is the evidence for this request. Check feature configuration and required filters before depending on this route. Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/main-page/blocks`

Read explorer homepage data — blocks.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/main-page/blocks`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/main-page/blocks'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
[
  {
    "base_fee_per_gas": "1000000000",
    "burnt_fees": "0",
    "burnt_fees_percentage": null,
    "difficulty": "0",
    "gas_limit": "4294967295",
    "gas_target_percentage": -100.0,
    "gas_used": "0",
    "gas_used_percentage": 0.0,
    "hash": "0x5a45faca9a8c98fe652affa072a9827bb6c396a0ca478e4f7b1d51fb3415adc8",
    "height": 3142006,
    "internal_transactions_count": null,
    "is_pending_update": false,
    "miner": {
      "ens_domain_name": null,
      "hash": "0xb49B53f2d258a17E0fcC9d97ad2b93CB3eF65dBD",
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
    "nonce": "0x0000000000000000",
    "parent_hash": "0x971e406f94869dc2c7b013e657f1914474bb380818bc0318986bee8a2623a8b7",
    "priority_fee": "0",
    "rewards": [],
    "size": 619,
    "timestamp": "2026-11-14T08:52:13.000000Z",
    "total_difficulty": null,
    "transaction_fees": "0",
    "transactions_count": 0,
    "type": "block",
    "uncles_hashes": [],
    "withdrawals_count": null
  }
]
```

### Response schema and errors

* HTTP `200`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
