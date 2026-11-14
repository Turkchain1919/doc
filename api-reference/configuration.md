# Configuration and Indexed Data API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/advanced-filters`

Read filtered indexed activity.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/advanced-filters`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `transaction_types` | query | no | string |
| `methods` | query | no | string |
| `age_from` | query | no | string |
| `age_to` | query | no | string |
| `age` | query | no | string |
| `from_address_hashes_to_include` | query | no | string |
| `from_address_hashes_to_exclude` | query | no | string |
| `to_address_hashes_to_include` | query | no | string |
| `to_address_hashes_to_exclude` | query | no | string |
| `address_relation` | query | no | string |
| `amount_from` | query | no | string |
| `amount_to` | query | no | string |
| `token_contract_address_hashes_to_include` | query | no | string |
| `token_contract_address_hashes_to_exclude` | query | no | string |
| `methods_names` | query | no | string |
| `token_contract_symbols_to_include` | query | no | string |
| `token_contract_symbols_to_exclude` | query | no | string |
| `block_number` | query | no | string; pattern `^([1-9][0-9]*&#124;0)$` |
| `transaction_index` | query | no | string; pattern `^([1-9][0-9]*&#124;0)$` |
| `internal_transaction_index` | query | no | value |
| `token_transfer_index` | query | no | value |
| `token_transfer_batch_index` | query | no | value |
| `items_count` | query | no | integer; min 1 |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/advanced-filters'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "status": "success",
      "timestamp": "2026-11-12T21:19:21.000000Z",
      "total": null,
      "type": "contract_interaction",
      "value": "0",
      "hash": "0x150593f23d7690822a16d10e202c3f504f0b3615a85196a9a6af089349235af4",
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
      "token": null,
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
      "method": "0x7c39d130",
      "block_number": 3117475,
      "transaction_index": 0,
      "fee": "175482546500000",
      "internal_transaction_index": null,
      "token_transfer_batch_index": null,
      "token_transfer_index": null,
      "created_contract": null
    }
  ],
  "next_page_params": {
    "block_number": 2948814,
    "transaction_index": 0,
    "internal_transaction_index": null,
    "token_transfer_batch_index": null,
    "token_transfer_index": null
  },
  "search_params": {
    "tokens": {},
    "methods": {}
  }
}
```

### Response schema and errors

* HTTP `200` — schema `AdvancedFilterResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/advanced-filters/methods`

Read filtered indexed activity — methods.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/advanced-filters/methods`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `q` | query | no | string |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/advanced-filters/methods'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
[
  {
    "name": "transfer",
    "method_id": "0xa9059cbb"
  }
]
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/config/backend`

Read deployment configuration — backend.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/config/backend`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/config/backend'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "chain_type": "default",
  "openapi_spec_folder_name": "default"
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/config/backend-version`

Read deployment configuration — backend-version.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/config/backend-version`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/config/backend-version'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "backend_version": "12.0.1"
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/config/db-background-migrations`

Read deployment configuration — db-background-migrations.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/config/db-background-migrations`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/config/db-background-migrations'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "migrations": [
    {
      "meta": {
        "step": "delete_not_whitelisted_weth_transfers"
      },
      "status": "wait_for_enabling_weth_filtering",
      "inserted_at": "2026-10-15T07:20:30.498139Z",
      "updated_at": "2026-10-15T07:20:30.533829Z",
      "migration_name": "sanitize_incorrect_weth_transfers"
    }
  ]
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/config/indexer`

Read deployment configuration — indexer.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/config/indexer`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/config/indexer'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "block_reward_fetcher_enabled": false,
  "indexer_enabled": true,
  "internal_transactions_fetcher_enabled": true,
  "pending_transactions_fetcher_enabled": false,
  "token_instance_retry_fetcher_enabled": true,
  "token_instance_sanitize_fetcher_enabled": true
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/config/public-metrics`

Read deployment configuration — public-metrics.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/config/public-metrics`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/config/public-metrics'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "update_period_hours": 24
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/main-page/indexing-status`

Read explorer homepage data — indexing-status.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/main-page/indexing-status`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/main-page/indexing-status'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "finished_indexing": false,
  "finished_indexing_blocks": true,
  "indexed_blocks_ratio": "1.00",
  "indexed_internal_transactions_ratio": "0.94"
}
```

### Response schema and errors

* HTTP `200`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
