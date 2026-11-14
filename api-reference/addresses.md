# Addresses API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/addresses`

Read indexed address records.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `sort` | query | no | string: `balance`, `transactions_count` |
| `order` | query | no | string: `asc`, `desc` |
| `items_count` | query | no | integer; min 1 |
| `fetched_coin_balance` | query | no | string; pattern `^-?([1-9][0-9]*&#124;0)$` |
| `hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `transactions_count` | query | no | value |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "transactions_count": "659",
      "coin_balance": "99997698655729057944103675546",
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
    }
  ],
  "total_supply": "0",
  "next_page_params": {
    "hash": "0x1b33c89e9b81fbbbe14aab6df0b78fe5af5dbac5",
    "transactions_count": 4,
    "fetched_coin_balance": "12000000000"
  },
  "exchange_rate": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `403` — schema `ForbiddenResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}`

Read indexed address records.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "block_number_balance_updated_at": 3117475,
  "coin_balance": "9999473528358100000",
  "creation_status": null,
  "creation_transaction_hash": null,
  "creator_address_hash": null,
  "ens_domain_name": null,
  "exchange_rate": null,
  "has_beacon_chain_withdrawals": false,
  "has_logs": false,
  "has_token_transfers": false,
  "has_tokens": false,
  "has_validated_blocks": false,
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
  "token": null,
  "watchlist_address_id": null,
  "watchlist_names": []
}
```

### Response schema and errors

* HTTP `200` — schema `AddressResponse`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/blocks-validated`

Read indexed address records — blocks-validated.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/blocks-validated`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/blocks-validated'
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
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/coin-balance-history`

Read indexed address records — coin-balance-history.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/coin-balance-history`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/coin-balance-history'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "block_number": 3117475,
      "block_timestamp": "2026-11-12T21:19:21Z",
      "delta": "-175482546500000",
      "transaction_hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
      "value": "9999473528358100000"
    }
  ],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/coin-balance-history-by-day`

Read indexed address records — coin-balance-history-by-day.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/coin-balance-history-by-day`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/coin-balance-history-by-day'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "date": "2026-11-08",
      "value": "10000000000000000000"
    }
  ],
  "days": 90
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/counters`

Read indexed address records — counters.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/counters`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/counters'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "transactions_count": "4",
  "token_transfers_count": "0",
  "gas_usage_count": "526419",
  "validations_count": "0"
}
```

### Response schema and errors

* HTTP `200` — schema `AddressCounters`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/internal-transactions`

Read indexed address records — internal-transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/internal-transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `filter` | query | no | string: `to`, `from` |
| `include_zero_value` | query | no | boolean |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |
| `index` | query | no | integer |
| `transaction_index` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/internal-transactions'
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
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/tabs-counters`

Read indexed address records — tabs-counters.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/tabs-counters`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/tabs-counters'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "transactions_count": 4,
  "token_transfers_count": 0,
  "withdrawals_count": 0,
  "validations_count": 0,
  "internal_transactions_count": 0,
  "logs_count": 0,
  "token_balances_count": 0
}
```

### Response schema and errors

* HTTP `200` — schema `AddressTabsCounters`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/token-balances`

Read indexed address records — token-balances.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/token-balances`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/token-balances'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
[]
```

### Response schema and errors

* HTTP `200`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/token-transfers`

Read indexed address records — token-transfers.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/token-transfers`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `filter` | query | no | string: `to`, `from` |
| `type` | query | no | value |
| `token` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | integer; min 0 |
| `index` | query | no | integer |
| `batch_log_index` | query | no | integer |
| `batch_block_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `batch_transaction_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `index_in_batch` | query | no | integer |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/token-transfers'
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
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/tokens`

Read indexed address records — tokens.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/tokens`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `type` | query | no | value |
| `items_count` | query | no | integer; min 1 |
| `fiat_value` | query | no | value |
| `id` | query | no | integer |
| `value` | query | no | value |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/tokens'
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
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/transactions`

Read indexed address records — transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `filter` | query | no | string: `to`, `from` |
| `sort` | query | no | string: `block_number`, `value`, `fee` |
| `order` | query | no | string: `asc`, `desc` |
| `items_count` | query | no | integer; min 1 |
| `block_number` | query | no | value |
| `index` | query | no | value |
| `inserted_at` | query | no | string |
| `hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{64})$` |
| `value` | query | no | value |
| `fee` | query | no | string; pattern `^-?([1-9][0-9]*&#124;0)$` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/transactions'
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
  ],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
