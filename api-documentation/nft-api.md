# NFT API

Read-only probes against the deployed TurkScan® API, captured 14 November 2026. Samples are historical data, not current balances or endorsements.

## GET `/api/v2/addresses/{address_hash_param}/nft`

Read indexed address records — nft.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/nft`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `type` | query | no | value |
| `items_count` | query | no | integer; min 1 |
| `token_contract_address_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `token_id` | query | no | string; pattern `^-?([1-9][0-9]*&#124;0)$` |
| `token_type` | query | no | string: `ERC-20`, `ERC-721`, `ERC-1155`, `ERC-404`, `ERC-7984`, `ERC-8056` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/nft'
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
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/addresses/{address_hash_param}/nft/collections`

Read indexed address records — nft, collections.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/nft/collections`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `type` | query | no | value |
| `items_count` | query | no | integer; min 1 |
| `token_contract_address_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `token_type` | query | no | string: `ERC-20`, `ERC-721`, `ERC-1155`, `ERC-404`, `ERC-7984`, `ERC-8056` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/addresses/0x5b491b52eF948f9A60D75d2a56235FbFB8644f0B/nft/collections'
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
* HTTP `403` — schema `ForbiddenResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/tokens/{address_hash_param}/instances`

Read indexed token records — instances.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `holder_address_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `items_count` | query | no | integer; min 1 |
| `unique_token` | query | no | string; pattern `^-?([1-9][0-9]*&#124;0)$` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "animation_media_type": null,
      "animation_url": null,
      "external_app_url": null,
      "id": "6",
      "image_media_type": "image",
      "image_url": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDI5MCA1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsnPjxkZWZzPjxmaWx0ZXIgaWQ9ImYxIj48ZmVJbWFnZSByZXN1bHQ9InAwIiB4bGluazpocmVmPSJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIzYVdSMGFEMG5Namt3SnlCb1pXbG5hSFE5SnpVd01DY2dkbWxsZDBKdmVEMG5NQ0F3SURJNU1DQTFNREFuSUhodGJHNXpQU2RvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeWMrUEhKbFkzUWdkMmxrZEdnOUp6STVNSEI0SnlCb1pXbG5hSFE5SnpVd01IQjRKeUJtYVd4c1BTY2pZMlF3WkRkaUp5OCtQQzl6ZG1jKyIvPjxmZUltYWdlIHJlc3VsdD0icDEiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwbk1qa3dKeUJvWldsbmFIUTlKelV3TUNjZ2 [excerpt]",
      "is_unique": true,
      "media_type": null,
      "media_url": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDI5MCA1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsnPjxkZWZzPjxmaWx0ZXIgaWQ9ImYxIj48ZmVJbWFnZSByZXN1bHQ9InAwIiB4bGluazpocmVmPSJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIzYVdSMGFEMG5Namt3SnlCb1pXbG5hSFE5SnpVd01DY2dkbWxsZDBKdmVEMG5NQ0F3SURJNU1DQTFNREFuSUhodGJHNXpQU2RvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeWMrUEhKbFkzUWdkMmxrZEdnOUp6STVNSEI0SnlCb1pXbG5hSFE5SnpVd01IQjRKeUJtYVd4c1BTY2pZMlF3WkRkaUp5OCtQQzl6ZG1jKyIvPjxmZUltYWdlIHJlc3VsdD0icDEiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwbk1qa3dKeUJvWldsbmFIUTlKelV3TUNjZ2 [excerpt]",
      "metadata": {
        "description": "This NFT represents a liquidity position in Turkchain v4 7777-8888 pool. The owner of this NFT can modify or redeem the position.\n\nPool Manager Address: 0xd5cd70a82739c4e54c5953c4c1adf4d6f55b134b\n7777 Address: 0xcd0d7b9eeec0897afcca0f0739ddecb830171271\n8888 Address: 0x34974f5c83915762e3ba9c487e09465c801ad9e3\nHook Address: No Hook\nFee Tier: 0.3%\nToken ID: 6\n\n⚠️ DISCLAIMER: Due diligence is imperative when assessing this NFT. Make sure currency addresses match the expected currencies, as currency symbols may be imitated.",
        "image": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDI5MCA1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsnPjxkZWZzPjxmaWx0ZXIgaWQ9ImYxIj48ZmVJbWFnZSByZXN1bHQ9InAwIiB4bGluazpocmVmPSJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIzYVdSMGFEMG5Namt3SnlCb1pXbG5hSFE5SnpVd01DY2dkbWxsZDBKdmVEMG5NQ0F3SURJNU1DQTFNREFuSUhodGJHNXpQU2RvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeWMrUEhKbFkzUWdkMmxrZEdnOUp6STVNSEI0SnlCb1pXbG5hSFE5SnpVd01IQjRKeUJtYVd4c1BTY2pZMlF3WkRkaUp5OCtQQzl6ZG1jKyIvPjxmZUltYWdlIHJlc3VsdD0icDEiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwbk1qa3dKeUJvWldsbmFIUTlKelV3TUNjZ2 [excerpt]",
        "name": "Turkchain - 0.3% - 7777/8888 - 0.49859<>0.99402"
      },
      "owner": {
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
      "thumbnails": null
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

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}`

Read indexed token records — instances.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `token_id_param` | path | yes | string; pattern `^-?([1-9][0-9]*&#124;0)$` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "animation_media_type": null,
  "animation_url": null,
  "external_app_url": null,
  "id": "1",
  "image_media_type": "image",
  "image_url": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDI5MCA1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsnPjxkZWZzPjxmaWx0ZXIgaWQ9ImYxIj48ZmVJbWFnZSByZXN1bHQ9InAwIiB4bGluazpocmVmPSJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIzYVdSMGFEMG5Namt3SnlCb1pXbG5hSFE5SnpVd01DY2dkbWxsZDBKdmVEMG5NQ0F3SURJNU1DQTFNREFuSUhodGJHNXpQU2RvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeWMrUEhKbFkzUWdkMmxrZEdnOUp6STVNSEI0SnlCb1pXbG5hSFE5SnpVd01IQjRKeUJtYVd4c1BTY2paV1ZpWXpNNEp5OCtQQzl6ZG1jKyIvPjxmZUltYWdlIHJlc3VsdD0icDEiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwbk1qa3dKeUJvWldsbmFIUTlKelV3TUNjZ2 [excerpt]",
  "is_unique": true,
  "media_type": null,
  "media_url": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDI5MCA1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsnPjxkZWZzPjxmaWx0ZXIgaWQ9ImYxIj48ZmVJbWFnZSByZXN1bHQ9InAwIiB4bGluazpocmVmPSJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIzYVdSMGFEMG5Namt3SnlCb1pXbG5hSFE5SnpVd01DY2dkbWxsZDBKdmVEMG5NQ0F3SURJNU1DQTFNREFuSUhodGJHNXpQU2RvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeWMrUEhKbFkzUWdkMmxrZEdnOUp6STVNSEI0SnlCb1pXbG5hSFE5SnpVd01IQjRKeUJtYVd4c1BTY2paV1ZpWXpNNEp5OCtQQzl6ZG1jKyIvPjxmZUltYWdlIHJlc3VsdD0icDEiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwbk1qa3dKeUJvWldsbmFIUTlKelV3TUNjZ2 [excerpt]",
  "metadata": {
    "description": "This NFT represents a liquidity position in Turkchain v4 6663-EEEE pool. The owner of this NFT can modify or redeem the position.\n\nPool Manager Address: 0xd5cd70a82739c4e54c5953c4c1adf4d6f55b134b\n6663 Address: 0xeebc38c8a5fa366fcb95caec2a9bb43439dee303\nEEEE Address: 0x9426771fa207cc8448ada556625235e2e2615f83\nHook Address: No Hook\nFee Tier: 0.3%\nToken ID: 1\n\n⚠️ DISCLAIMER: Due diligence is imperative when assessing this NFT. Make sure currency addresses match the expected currencies, as currency symbols may be imitated.",
    "image": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDI5MCA1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsnPjxkZWZzPjxmaWx0ZXIgaWQ9ImYxIj48ZmVJbWFnZSByZXN1bHQ9InAwIiB4bGluazpocmVmPSJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIzYVdSMGFEMG5Namt3SnlCb1pXbG5hSFE5SnpVd01DY2dkbWxsZDBKdmVEMG5NQ0F3SURJNU1DQTFNREFuSUhodGJHNXpQU2RvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeWMrUEhKbFkzUWdkMmxrZEdnOUp6STVNSEI0SnlCb1pXbG5hSFE5SnpVd01IQjRKeUJtYVd4c1BTY2paV1ZpWXpNNEp5OCtQQzl6ZG1jKyIvPjxmZUltYWdlIHJlc3VsdD0icDEiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwbk1qa3dKeUJvWldsbmFIUTlKelV3TUNjZ2 [excerpt]",
    "name": "Turkchain - 0.3% - 6663/EEEE - MIN<>MAX"
  },
  "owner": {
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
  "thumbnails": null,
  "token": {
    "address_hash": "0x4546402D50386B42883BD15960054440B8E96B74",
    "circulating_market_cap": null,
    "circulating_supply": null,
    "decimals": null,
    "exchange_rate": null,
    "holders_count": "5",
    "icon_url": null,
    "name": "Turkchain v4 Positions NFT",
    "new_ui_multiplier": null,
    "reputation": "ok",
    "symbol": "TURK-V4-POSM",
    "total_supply": null,
    "type": "ERC-721",
    "ui_multiplier": null,
    "ui_multiplier_effective_at": null,
    "volume_24h": null
  }
}
```

### Response schema and errors

* HTTP `200` — schema `TokenInstance`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/holders`

Read indexed token records — instances, holders.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1/holders`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `token_id_param` | path | yes | string; pattern `^-?([1-9][0-9]*&#124;0)$` |
| `items_count` | query | no | integer; min 1 |
| `address_hash` | query | no | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `token_id` | query | no | string; pattern `^-?([1-9][0-9]*&#124;0)$` |
| `value` | query | no | value |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1/holders'
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


## GET `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/transfers`

Read indexed token records — instances, transfers.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1/transfers`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `token_id_param` | path | yes | string; pattern `^-?([1-9][0-9]*&#124;0)$` |
| `items_count` | query | no | integer; min 1 |
| `index` | query | no | integer |
| `block_number` | query | no | integer; min 0 |
| `token_id` | query | no | string; pattern `^-?([1-9][0-9]*&#124;0)$` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1/transfers'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "items": [
    {
      "block_hash": "0x9a9a6bfcb5abd2a6ab6259a07437480bff41ca0114db5f765354d00bf9d171b7",
      "block_number": 2647412,
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
      "log_index": 1,
      "method": "0xac9650d8",
      "timestamp": "2026-10-15T11:36:44.000000Z",
      "to": {
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
      "token": {
        "address_hash": "0x4546402D50386B42883BD15960054440B8E96B74",
        "circulating_market_cap": null,
        "circulating_supply": null,
        "decimals": null,
        "exchange_rate": null,
        "holders_count": "5",
        "icon_url": null,
        "name": "Turkchain v4 Positions NFT",
        "new_ui_multiplier": null,
        "reputation": "ok",
        "symbol": "TURK-V4-POSM",
        "total_supply": null,
        "type": "ERC-721",
        "ui_multiplier": null,
        "ui_multiplier_effective_at": null,
        "volume_24h": null
      },
      "token_type": "ERC-721",
      "total": {
        "token_id": "1",
        "token_instance": null
      },
      "transaction_hash": "0x3ad36090c61c43e28951d340aaa18f571269c9a4e7c38b835c85798449d8db42",
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

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.


## GET `/api/v2/tokens/{address_hash_param}/instances/{token_id_param}/transfers-count`

Read indexed token records — instances, transfers-count.

**Observed:** HTTP 200 on 14 November 2026. Read succeeded; an empty result remains a valid empty result.

**Exact tested URL:** `https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1/transfers-count`

### Parameters and required fields

| Name | Location | Required | Type / allowed values |
| --- | --- | --- | --- |
| `apikey` | query | no | string |
| `key` | query | no | string |
| `address_hash_param` | path | yes | string; pattern `^0x([A-Fa-f0-9]{40})$` |
| `token_id_param` | path | yes | string; pattern `^-?([1-9][0-9]*&#124;0)$` |

Path identifiers must be URL-encoded and supplied in full. For list endpoints, also preserve any resource-specific fields returned in `next_page_params`. `apikey` is an optional account key where configured; `key` is not a public shared credential.

### Example request

```bash
curl --fail-with-body 'https://turkscan.com/api/v2/tokens/0x4546402D50386B42883BD15960054440B8E96B74/instances/1/transfers-count'
```

### Observed response

HTTP 200. List examples retain only the first item, and long strings may be excerpted; [complete capture](../reference/endpoint-evidence.json) retains the original response.

```json
{
  "transfers_count": 1
}
```

### Response schema and errors

* HTTP `200`.
* HTTP `404` — schema `NotFoundResponse`.
* HTTP `422` — schema `JsonErrorResponse`.

Schema declarations describe possible results, not proof of success. Also handle proxy/service errors and 429 with bounded retries. See [Error Handling](error-handling.md).

### Usage notes

Keep integer strings precise and null fields unavailable. Indexed data can lag node state. The stored [OpenAPI snapshot](../reference/openapi.json) provides full field definitions; [pagination](pagination.md) explains list cursors.
