# Tokens API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/token-transfers`

Read token transfer events.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/token-transfers`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
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
curl --fail-with-body 'https://turkscan.com/api/v2/token-transfers'
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
      "method": "0x7c39d130",
      "timestamp": "2026-11-12T21:19:21.000000Z",
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
  "next_page_params": {
    "index": 0,
    "block_number": 2557586
  }
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/tokens/`

Read indexed token records.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `type` | query | no | value |
| `q` | query | no | string |
| `limit` | query | no | integer |
| `sort` | query | no | string: `fiat_value`, `holders_count`, `circulating_market_cap` |
| `order` | query | no | string: `asc`, `desc` |
| `items_count` | query | no | integer; min 1 |
| `contract_address_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `fiat_value` | query | no | value |
| `holders_count` | query | no | value |
| `is_name_null` | query | no | boolean |
| `market_cap` | query | no | value |
| `name` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "address_hash": "0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271",
      "circulating_market_cap": null,
      "circulating_supply": null,
      "decimals": "18",
      "exchange_rate": null,
      "holders_count": "6",
      "icon_url": null,
      "name": "777",
      "new_ui_multiplier": null,
      "reputation": "ok",
      "symbol": "7777",
      "total_supply": "1000000000000000000000000",
      "type": "ERC-20",
      "ui_multiplier": null,
      "ui_multiplier_effective_at": null,
      "volume_24h": null
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


## GET `/api/v2/tokens/{address_hash_param}`

Read indexed token records.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "address_hash": "0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271",
  "circulating_market_cap": null,
  "circulating_supply": null,
  "decimals": "18",
  "exchange_rate": null,
  "holders_count": "6",
  "icon_url": null,
  "name": "777",
  "new_ui_multiplier": null,
  "reputation": "ok",
  "symbol": "7777",
  "total_supply": "1000000000000000000000000",
  "type": "ERC-20",
  "ui_multiplier": null,
  "ui_multiplier_effective_at": null,
  "volume_24h": null
}
```

### Response schema and errors

* HTTP `200` — schema `TokenResponse`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/tokens/{address_hash_param}/counters`

Read indexed token records — counters.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/counters`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/counters'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "transfers_count": "128889",
  "token_holders_count": "6",
  "ui_multiplier_changes_count": "0"
}
```

### Response schema and errors

* HTTP `200` — schema `TokenCountersResponse`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/tokens/{address_hash_param}/holders`

Read indexed token records — holders.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/holders`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `items_count` | query | no | integer; min 1 |
| `address_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `value` | query | no | value |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/holders'
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
      "token_id": null,
      "value": "557348745844634010031909"
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


## GET `/api/v2/tokens/{address_hash_param}/transfers`

Read indexed token records — transfers.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/transfers`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
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
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271/transfers'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "block_hash": "0x602aa39e12f7ee708f430d0a9d6fa665a8d52bbc45bf1827cb3c380ae2845276",
      "block_number": 2742182,
      "from": {
        "ens_domain_name": null,
        "hash": "0x3F62cE857EDb2E2B2ee80a4FbcE59fE7B943088a",
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
      "log_index": 1,
      "method": "0x3593564c",
      "timestamp": "2026-10-21T07:28:22.000000Z",
      "to": {
        "ens_domain_name": null,
        "hash": "0xd5cd70a82739C4e54C5953c4c1Adf4D6F55B134b",
        "implementations": [],
        "is_contract": true,
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
      "token": {
        "address_hash": "0xCD0d7B9eEEc0897aFCcA0f0739DDECb830171271",
        "circulating_market_cap": null,
        "circulating_supply": null,
        "decimals": "18",
        "exchange_rate": null,
        "holders_count": "6",
        "icon_url": null,
        "name": "777",
        "new_ui_multiplier": null,
        "reputation": "ok",
        "symbol": "7777",
        "total_supply": "1000000000000000000000000",
        "type": "ERC-20",
        "ui_multiplier": null,
        "ui_multiplier_effective_at": null,
        "volume_24h": null
      },
      "token_type": "ERC-20",
      "total": {
        "decimals": "18",
        "ui_multiplier": null,
        "value": "5000000000000000000"
      },
      "transaction_hash": "0xeb339f14cdcac4bba9197951ed90109139bbb4911e711503e17954181406ba9f",
      "type": "token_transfer"
    }
  ],
  "next_page_params": {
    "index": 0,
    "block_number": 1127174
  }
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
