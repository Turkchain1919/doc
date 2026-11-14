# Statistics API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/stats`

Read network statistics.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/stats`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/stats'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "average_block_time": 5232.0,
  "coin_image": null,
  "coin_price": null,
  "coin_price_change_percentage": null,
  "gas_price_updated_at": "2026-11-14T08:51:55.662633Z",
  "gas_prices": {
    "slow": 0.88,
    "average": 0.88,
    "fast": 0.88
  },
  "gas_prices_update_in": 3552,
  "gas_used_today": null,
  "market_cap": "0",
  "network_utilization_percentage": 0.0,
  "secondary_coin_image": null,
  "secondary_coin_price": null,
  "static_gas_price": null,
  "total_addresses": "45941",
  "total_blocks": "3141996",
  "total_transactions": "239420",
  "transactions_today": "0",
  "tvl": null
}
```

### Response schema and errors

* HTTP `200` — schema `StatsResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/stats/charts/market`

Read network statistics — charts, market.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/stats/charts/market`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/stats/charts/market'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "available_supply": 0,
  "chart_data": []
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/stats/charts/secondary-coin-market`

Read network statistics — charts, secondary-coin-market.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/stats/charts/secondary-coin-market`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/stats/charts/secondary-coin-market'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "chart_data": []
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/stats/charts/transactions`

Read network statistics — charts, transactions.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/stats/charts/transactions`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/stats/charts/transactions'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "chart_data": [
    {
      "date": "2026-11-13",
      "transactions_count": 0
    }
  ]
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/stats/hot-smart-contracts`

Read network statistics — hot-smart-contracts.

**Observed:** HTTP 422 on 14 November 2026. This probe did not succeed. Do not treat this operation as an available feature without resolving the reported condition.

**Exact tested URL:** `https://turkscan.com/api/v2/stats/hot-smart-contracts`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `sort` | query | no | string: `transactions_count`, `total_gas_used` |
| `order` | query | no | string: `asc`, `desc` |
| `scale` | query | yes | string: `5m`, `1h`, `3h`, `1d`, `7d`, `30d` |
| `items_count` | query | no | integer; min 1 |
| `transactions_count` | query | no | integer; min 1 |
| `total_gas_used` | query | no | integer; min 0 |
| `contract_address_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/stats/hot-smart-contracts'
```

### Observed response

HTTP 422. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "errors": [
    {
      "title": "Invalid value",
      "source": {
        "pointer": "/scale"
      },
      "detail": "Missing field: scale"
    }
  ]
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

The captured failure is the evidence for this request. Check feature configuration and required filters before depending on this route. Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
