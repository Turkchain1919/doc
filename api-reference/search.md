# Search API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/search`

Read search results.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/search?q=TURK`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `q` | query | no | string |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `next_page_params_type` | query | no | string |
| `label` | query | no | object |
| `token` | query | no | object |
| `contract` | query | no | object |
| `tac_operation` | query | no | object |
| `metadata_tag` | query | no | object |
| `block` | query | no | object |
| `blob` | query | no | object |
| `user_operation` | query | no | object |
| `address` | query | no | object |
| `ens_domain` | query | no | object |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/search?q=TURK'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "address_hash": "0x2C52471d39f35dFc6A930Ba276a027ECbfC09706",
      "address_url": "/address/0x2C52471d39f35dFc6A930Ba276a027ECbfC09706",
      "certified": false,
      "circulating_market_cap": null,
      "exchange_rate": null,
      "icon_url": "https://turkscan.com/uploads/f967ccee34903ff49f90f56a25b4bb1557c65dc94c3049589034a1d6744540fd.png",
      "is_smart_contract_address": true,
      "is_smart_contract_verified": false,
      "is_verified_via_admin_panel": true,
      "name": "Wrapped TURK",
      "priority": 2,
      "reputation": "ok",
      "symbol": "WTURK",
      "token_type": "ERC-20",
      "token_url": "/token/0x2C52471d39f35dFc6A930Ba276a027ECbfC09706",
      "total_supply": "5000000000000000000",
      "type": "token"
    }
  ],
  "next_page_params": null
}
```

### Response schema and errors

* HTTP `200` — schema `SearchResult`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/search/check-redirect`

Read search results — check-redirect.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/search/check-redirect?q=TURK`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `q` | query | no | string |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/search/check-redirect?q=TURK'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
{
  "parameter": null,
  "redirect": false,
  "type": null
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/search/quick`

Read search results — quick.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/search/quick?q=TURK`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `q` | query | no | string |
| `apikey` | query | no | string |
| `key` | query | no | string |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/search/quick?q=TURK'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](reference/endpoint-evidence.json) retains the original response.

```json
[
  {
    "address_hash": "0x2C52471d39f35dFc6A930Ba276a027ECbfC09706",
    "address_url": "/address/0x2C52471d39f35dFc6A930Ba276a027ECbfC09706",
    "certified": false,
    "circulating_market_cap": null,
    "exchange_rate": null,
    "icon_url": "https://turkscan.com/uploads/f967ccee34903ff49f90f56a25b4bb1557c65dc94c3049589034a1d6744540fd.png",
    "is_smart_contract_address": true,
    "is_smart_contract_verified": false,
    "is_verified_via_admin_panel": true,
    "name": "Wrapped TURK",
    "priority": 2,
    "reputation": "ok",
    "symbol": "WTURK",
    "token_type": "ERC-20",
    "token_url": "/token/0x2C52471d39f35dFc6A930Ba276a027ECbfC09706",
    "total_supply": "5000000000000000000",
    "type": "token"
  }
]
```

### Response schema and errors

* HTTP `200`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
